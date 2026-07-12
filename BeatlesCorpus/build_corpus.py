#!/usr/bin/env python3
"""Merge Isophonics (chords/keys/segments) + BeatlesFC (T/PD/D functions)
into per-song Roman-numeral analyses and a transition index.

Conventions match chronoVoyant/MusicTheory/AXIOMS.md:
- Roman numerals relative to the MAJOR scale of the local key tonic
  (minor-key songs: tonic chord = i, relative degrees like bIII, bVI, bVII).
- Uppercase major, lowercase minor, ° diminished, ø half-diminished,
  + augmented; extensions kept as suffixes (V7, ii7, IVmaj7).
"""
import os, re, sys
from collections import defaultdict

SCRATCH = os.path.dirname(os.path.abspath(__file__))
ISO = os.path.join(SCRATCH, "isophonics")
FC = os.path.join(SCRATCH, "beatlesFC")
OUT = "/Users/kyleriche/Desktop/chronoVoyant/BeatlesCorpus"

PC = {"C":0,"D":2,"E":4,"F":5,"G":7,"A":9,"B":11}
def pitch_class(name):
    pc = PC[name[0].upper()]
    for ch in name[1:]:
        if ch == "#": pc += 1
        elif ch == "b": pc -= 1
    return pc % 12

DEGREE = {0:"I",1:"bII",2:"II",3:"bIII",4:"III",5:"IV",6:"bV",7:"V",8:"bVI",9:"VI",10:"bVII",11:"VII"}

def parse_chord(label):
    """Harte syntax -> (root, quality, ext, bass) or None for N/X."""
    if label in ("N","X"): return None
    m = re.match(r"^([A-G][#b]*)(?::([^/]*))?(?:/(.*))?$", label)
    if not m: return None
    root, qual, bass = m.group(1), m.group(2) or "maj", m.group(3)
    return root, qual, bass

def numeral(root, qual, bass, key_pc):
    iv = (pitch_class(root) - key_pc) % 12
    deg = DEGREE[iv]
    q = qual
    minorish = q.startswith("min")
    dim = q.startswith("dim")
    hdim = q.startswith("hdim")
    aug = q.startswith("aug")
    base = deg.lower() if (minorish or dim or hdim) else deg
    # extension suffix
    ext = ""
    if q not in ("maj","min"):
        ext = q.replace("min","").replace("maj","maj") if False else q
        # normalize: strip leading quality word for display
        for pre in ("min","maj","dim","hdim","aug"):
            if ext.startswith(pre) and len(ext) > len(pre):
                ext = ext[len(pre):]
                break
        if ext in ("min","dim","aug","hdim"): ext = ""
        if q.startswith("maj") and q not in ("maj",):  # maj7 etc.
            ext = q[3:] and ("maj"+q[3:]) or ""
    mark = "°" if dim else ("ø" if hdim else ("+" if aug else ""))
    inv = f"/{bass}" if bass else ""
    return f"{base}{mark}{ext}{inv}"

def read_lab(path, sep=None):
    rows = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3:
                try:
                    rows.append((float(parts[0]), float(parts[1]), " ".join(parts[2:])))
                except ValueError:
                    pass
    return rows

def lookup(rows, t):
    for s,e,v in rows:
        if s - 0.05 <= t < e - 0.01:
            return v
    return None

def song_paths():
    """Yield (album, track, chordfile, keyfile, segfile, fcA, fcB)."""
    croot = os.path.join(ISO, "chordlab", "The Beatles")
    for album in sorted(os.listdir(croot)):
        adir = os.path.join(croot, album)
        if not os.path.isdir(adir): continue
        for f in sorted(os.listdir(adir)):
            if not f.endswith(".lab"): continue
            base = f[:-4]
            key = os.path.join(ISO,"keylab","The Beatles",album,f)
            seg = os.path.join(ISO,"seglab","The Beatles",album,f)
            fca = os.path.join(FC, album, base + "_func_A.lab")
            fcb = os.path.join(FC, album, base + "_func_B.lab")
            if not (os.path.exists(fca) or os.path.exists(fcb)):
                # punctuation differs between the datasets: match on
                # alphanumerics only
                fcdir = os.path.join(FC, album)
                norm = re.sub(r"[^A-Za-z0-9]", "", base).lower()
                if os.path.isdir(fcdir):
                    for g in os.listdir(fcdir):
                        if not g.endswith(".lab"): continue
                        m2 = re.match(r"^(.*)_func_([AB])\.lab$", g)
                        stem = m2.group(1) if m2 else g[:-4]
                        which = m2.group(2) if m2 else "A"
                        gn = re.sub(r"[^A-Za-z0-9]", "", stem).lower()
                        # exact or prefix match either way (dataset
                        # filenames truncate/expand titles); guard len
                        if gn == norm or (min(len(gn), len(norm)) >= 6
                                and (gn.startswith(norm) or norm.startswith(gn))):
                            if which == "A": fca = os.path.join(fcdir, g)
                            else: fcb = os.path.join(fcdir, g)
            yield (album, base, os.path.join(adir,f),
                   key if os.path.exists(key) else None,
                   seg if os.path.exists(seg) else None,
                   fca if os.path.exists(fca) else None,
                   fcb if os.path.exists(fcb) else None)

def fmt_t(sec):
    m, s = divmod(int(sec), 60)
    return f"{m}:{s:02d}"

def main():
    os.makedirs(os.path.join(OUT, "songs"), exist_ok=True)
    transitions = defaultdict(list)   # (num1,num2) -> [(song, segment)]
    n_songs = 0; n_skipped = []
    for album, track, cpath, kpath, spath, fca, fcb in song_paths():
        primary = fca or fcb
        if not (kpath and primary):
            n_skipped.append(f"{album}/{track}" + (" (no key)" if not kpath else " (no FC)"))
            continue
        annot = "A" if fca else "B"
        fca = primary
        chords = read_lab(cpath)
        keys = [(s,e,v.split()[-1]) for s,e,v in read_lab(kpath) if v.startswith("Key")]
        # key rows: value like "Key E" -> tonic token last
        keys = [(s,e,v) for s,e,v in keys]
        if not keys:
            # some files: "Key\tE" splits to ['Key','E'] handled above; if still empty, skip
            n_skipped.append(f"{album}/{track} (no key rows)"); continue
        segs = read_lab(spath) if spath else []
        funcs = read_lab(fca)
        events = []
        for s,e,label in chords:
            pc = parse_chord(label)
            if pc is None: continue
            keyv = lookup(keys, s)
            if not keyv: continue
            tonic = keyv.split(":")[0]
            mode = keyv.split(":")[1] if ":" in keyv else "major"
            num = numeral(pc[0], pc[1], pc[2], pitch_class(tonic))
            func = lookup(funcs, s) or "?"
            seg = lookup(segs, s) or ""
            events.append((s, e, label, num, func, seg, tonic, mode))
        if not events:
            n_skipped.append(f"{album}/{track} (no events)"); continue
        n_songs += 1
        # per-song file
        title = track.split("_-_")[-1].replace("_"," ")
        album_title = album.split("_-_",1)[-1].replace("_"," ")
        adir = os.path.join(OUT, "songs", album)
        os.makedirs(adir, exist_ok=True)
        lines = [f"# {title}", "",
                 f"- Album: {album_title}",
                 "- Key: (filled below)",
                 f"- Sources: Isophonics chords/keys/segments + BeatlesFC functions (annotator {annot}" + ("; both A and B versions exist" if (fca and fcb and annot=='A') else "") + ")",
                 "", "Function labels: T = tonic/stable, PD = predominant, D = dominant (Nobile functional circuit).", ""]
        # fix Key line (built awkwardly above)
        keyset = sorted({(e[6], e[7]) for e in events})
        lines[3] = "- Key: " + ", ".join(f"{t} {m}" if m != "major" else t for t, m in keyset)
        cur_seg = object()
        run = []  # condensed within segment: (num, func, start)
        def flush(seg_name, run):
            if not run: return
            lines.append(f"**{seg_name or 'section'}** [{fmt_t(run[0][2])}]")
            lines.append("")
            lines.append("`" + "  ".join(f"{n}({f})" for n,f,_ in run) + "`")
            lines.append("")
        prev = None
        for s,e,label,num,func,seg,tonic,mode in events:
            if seg != cur_seg:
                flush(cur_seg if cur_seg is not object else "", run); run = []; cur_seg = seg
                prev = None
            if prev and prev[0] == num and prev[1] == func:
                continue  # condense repeats
            run.append((num, func, s))
            if prev and prev[0] != num:
                # strip extensions/inversions for transition key
                def core(n): return re.sub(r"(maj)?[0-9()/#b].*$","",n) or n
                a, b = core(prev[0]), core(num)
                if a != b:
                    transitions[(a,b)].append((title, seg or "?"))
            prev = (num, func)
        flush(cur_seg if cur_seg is not object else "", run)
        with open(os.path.join(adir, track + ".md"), "w") as f:
            f.write("\n".join(lines) + "\n")
    # transition index
    idx = ["# Transition Index", "",
           "Every chord-to-chord move in the corpus (Roman numerals relative to",
           "the local key's major scale, extensions stripped), with song and",
           "section. Cross-reference with MusicTheory/AXIOMS.md section 4-5.", ""]
    for (a,b), occs in sorted(transitions.items(), key=lambda kv: -len(kv[1])):
        if len(occs) < 2: continue
        songs = sorted({f"{s} ({seg})" for s,seg in occs})
        idx.append(f"## {a} → {b}  — {len(occs)} occurrences in {len({s for s,_ in occs})} songs")
        idx.append("")
        idx.append("; ".join(songs[:12]) + (f"; … +{len(songs)-12} more" if len(songs) > 12 else ""))
        idx.append("")
    with open(os.path.join(OUT, "INDEX.md"), "w") as f:
        f.write("\n".join(idx) + "\n")
    print(f"songs written: {n_songs}")
    print(f"skipped: {len(n_skipped)}")
    for s in n_skipped[:10]: print("  -", s)
    print(f"distinct transitions (>=2 occ): {sum(1 for k,v in transitions.items() if len(v)>=2)}")

if __name__ == "__main__":
    main()
