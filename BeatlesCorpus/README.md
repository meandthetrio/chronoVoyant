# Beatles Corpus

Real-song harmonic examples for crafting: 175 Beatles songs with
timestamped chords, keys, song structure, and expert harmonic-function
labels — merged into Roman-numeral analyses that speak the same
language as [MusicTheory/AXIOMS.md](../MusicTheory/AXIOMS.md).

## What's here

- **`songs/<album>/<track>.md`** — one file per song: key(s), then each
  structural section (verse, refrain, bridge…) with its progression as
  Roman numerals, each chord tagged with its harmonic function:
  `T` (tonic/stable), `PD` (predominant), `D` (dominant) — Nobile's
  functional-circuit labels, i.e. the harmonic version of Pattison's
  stable/unstable axis in [SongCraft/AXIOMS.md](../SongCraft/AXIOMS.md).
- **`INDEX.md`** — every chord-to-chord move in the corpus (≥2
  occurrences), ranked by frequency, with the songs and sections where
  it happens. Use it to hear real examples of any transition in the
  MusicTheory axiom map (e.g. look up `bVII → I` for backdoor
  resolutions, `vi → IV` for the redemption move).
- **`data/`** — the raw source datasets, kept verbatim as provenance.
- **`build_corpus.py`** — the script that generated `songs/` and
  `INDEX.md` from `data/`. Deterministic; re-run to regenerate.

## Conventions

- Roman numerals are relative to the **major scale of the local key
  tonic** (matching MusicTheory/AXIOMS.md): uppercase major, lowercase
  minor, ° diminished, ø half-diminished, + augmented; extensions and
  inversions kept as suffixes (`V7`, `ii7`, `vi/5`). Minor-key songs
  therefore show their tonic as `i` and relative degrees as `bIII`,
  `bVI`, `bVII`.
- Modulations use Isophonics' key labels as local keys, per the
  BeatlesFC paper's own method.
- The transition index strips extensions/inversions, so `V7 → I` and
  `V → I` count together.

## Sources & attribution

- **Isophonics reference annotations** (chords, keys, segments):
  Christopher Harte, *Towards Automatic Extraction of Harmony
  Information from Music Signals*, PhD thesis, Queen Mary University
  of London, 2010. Downloaded from https://isophonics.net/datasets.
- **BeatlesFC harmonic function annotations**: J.Y. Sim, R. Moranis,
  and J. Devaney, "BeatlesFC: Harmonic function annotations of
  Isophonics' The Beatles dataset," ISMIR 2024 Late-Breaking/Demo;
  arXiv:2601.02099 (Jan 2026). CC BY 4.0.
  https://github.com/jcdevaney/beatlesFC — annotator A's files are
  used where both exist; songs analyzed only by annotator B use the
  `_func_B` files (the per-song header says which).
- Theoretical basis: Drew Nobile, "Harmonic Function in Rock Music: A
  Syntactical Approach" (JMT 2016) and *Form as Harmony in Rock Music*
  (OUP 2020).

Coverage: 179 of 180 Isophonics songs — the full BeatlesFC set. The
only exclusion is Revolution 9 (no discernible key; excluded by the
BeatlesFC authors). Filenames differ slightly between the two datasets
(punctuation, truncated titles), so `build_corpus.py` matches songs on
normalized names.

## How this is used in chronoVoyant

This corpus is **evidence, not axioms**: the axiom layers say what a
move feels like; this corpus shows where the Beatles actually made
that move, in which section, with what function context. Typical uses:

- Ground a suggestion: "the map points at iv→I for this claim — here
  are the Beatles songs that do it, jump to the timestamp and listen."
- Check an axiom against reality (T ≈ 70% of all labels: stability
  dominates even in adventurous writing).
- Study a form: pull every `bridge` section and see what functions
  bridges actually sit on.
