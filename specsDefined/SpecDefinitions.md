# Spec Definitions

The four areas where the objective system operates — the four strengths
named in THE_BIBLE.md. Status: **all four SETTLED, 2026-07-11.** Each
definition was refined in conversation and adopted with the artist's
explicit approval. Song work (song folders, per-song files) can now
begin. Amendments to a settled definition follow the same rule as
everything else: proposed in conversation, written only with approval.

---

## Everything declarative

**Status: SETTLED — 2026-07-11.**

Holding declared intent against the artifact. A song declares what it is
— early, while intent is still clean — and every draft is checked against
that declaration. Drift is reported with zero fatigue and zero
politeness. Breaking a declaration is allowed, but only as a recorded
choice, never as unnoticed drift.

**What a declaration contains.** A required core plus optional
extensions:

- **Core** (must exist before the first audit): **POV** (person, and who
  the "you" is if there is one), **tense**, **setting** (the concrete
  anchor — where and when the song lives), **the claim** — one
  sentence stating what the song is about, specific enough to drift
  from — **mode**: **testimony** (first-person truth is the
  material) or **script** (invented characters; Murphy-mode) — and
  **audience clock**: **7 a.m.** (the drive-time listener; the full
  Murphy doctrines audit at strength) or **10 p.m.** (the room; a
  different, legitimate craft — frequent deliberate deviation from the
  7 a.m. doctrines is expected and logged as choice, like any
  deviation). *(Mode added 2026-07-11 via SongCraft doctrine D5,
  scoped; audience clock added 2026-07-11 via doctrine D7 — see
  SongCraft/AXIOMS.md.)* In both modes the claim must be true of the
  artist: characters may be invented, the reason for writing may not.
- **Extensions** (optional, each timestamped when added): form, hook
  placement, rhyme scheme, title, tempo/key, anything else the artist
  wants held.

Only declared dimensions are audited — an undeclared dimension can't
drift, so declaring a field is opting into being held to it. The
*content* of every field is the artist's (a Feel decision); the system
enforces that the fields exist and audits against them. It never
suggests what to declare.

**When it's made.** The declaration is a song's birth certificate, not a
precondition for writing. Fragments and captures live free, no
declaration needed. The moment something becomes a song in progress —
gets a folder, gets drafted against — the core declaration must exist
before the first audit. No declared core, no audit; no undeclared song
accumulates drafts in the system.

**When draft and declaration disagree.** Drift is reported specifically
and mechanically. The artist resolves each finding with exactly one of
three paths; nothing auto-resolves:

1. **Fix the draft** — it was drift; the draft is corrected.
2. **Deliberate deviation** — the declaration stands; the break is
   logged as a choice in the deviation log. Rule-breaking stays
   artistic, never accidental.
3. **Amend the declaration** — intent genuinely changed. Amendments are
   append-only: prior versions stay in the history with a dated reason.
   Rewriting the declaration to match the draft is the songwriting
   version of moving a stop, so amendments are legal but visible — a
   song's amendment count is itself a process statistic.

## Craft mechanics

**Status: SETTLED — 2026-07-11.**

The measurable mechanics of lyric and arrangement — the
trading-indicator layer of songwriting, complex but objective. All six
checks are active:

1. **Prosody** — natural word stress against the strong beats of the
   melody; collisions flagged line by line.
2. **Rhyme scheme consistency** — the pattern a section establishes,
   held against every later section; slips are flagged as drift unless
   marked as deviations.
3. **Syllable counts against melody** — line lengths counted against the
   established melodic rhythm; cram and stretch points flagged.
4. **Harmonic analysis** — key, chord function, resolution and refusal,
   whether a section goes somewhere harmonically new.
5. **Section proportions** — the structural clock: bar counts, section
   lengths, time to first vocal, time to hook.
6. **Concrete vs. abstract imagery** — each line classified as pointing
   at a thing in the world or a category of feeling; counts and
   distribution reported. (Overlaps with the truth-avoidance detector,
   which asks what an abstract line is avoiding; here it's the raw
   measurement.)

A check runs only when the draft supplies what it reads: no melody, no
prosody or syllable audit; no chords, no harmonic analysis.

Findings are **diagnostics, never verdicts**: "this stressed syllable
fights the beat" is information; what to do about it is a Feel decision.
Plenty of great songs break these rules on purpose — the system's job is
making sure the break is on purpose.

## Process and statistics

**Status: SETTLED — 2026-07-11.**

The trading journal, applied to music. The benefit is not the tracking
itself: it's that the record answers questions memory can't, because
memory edits itself and a log doesn't. No single session looks like the
reason an album doesn't get finished; the reason only exists in the
aggregate. Most unfinished albums die from process failure, not talent
failure, and process is fully objectifiable.

**Collection is passive.** The work lives in this repo, so git already
timestamps every capture, draft, and touch of every file — most
statistics fall out of history generated just by working. The only
manual addition is a minimal session note (a line or two: what was
worked on, what state it was left in). Logging must never become its own
job.

**Statistics are reported periodically**, aimed at the questions recall
can't answer: where songs actually stall, which kinds of starts convert
to finished songs, how long songs sit in "almost done" (a song that
feels active but hasn't been touched in months is the log's single most
valuable finding), and which themes recur in the journal but never reach
a lyric — that last one feeds the truth-avoidance detector.

**Rules come from evidence, never upfront.** No rules are adopted at the
start; any rule invented before the record exists is a guess. A rule
earns its place only when it points at a pattern the record has
demonstrated (e.g., "songs untouched for 30 days get a decision: revive
or shelve"), and every rule is adopted only with the artist's explicit
approval. Rules are responses to evidence, not resolutions.

## The truth-avoidance detector

**Status: SETTLED — 2026-07-11.**

Whether a line is true is subjective — only the artist knows. Whether a
line is *specific* is objective, and vagueness is where avoidance hides:
a lyric that states a feeling instead of showing a scene is the
songwriting equivalent of a rationalized trade.

**How flagging works.** The detector runs line by line in the same audit
pass as everything else, on top of the concrete-vs-abstract
classification from craft check #6. Every abstract line gets one flag
and one question — never a rewrite, never a suggested alternative. The
question depends on the song's declared **mode** *(amendment
2026-07-11, from SongCraft doctrine D5 scoped)*: in a **testimony**
song it is **"what actually happened?"**, at full strength — an
invented specific standing in for an unfaced true thing is itself
avoidance; in a **script** song it is **"what happens in this
story?"** — vagueness remains a defect, as craft rather than honesty,
and invention is legal. In both modes the declaration's claim must be
true of the artist. Flagging is uniform across sections (choruses
included); the deliberate mark is what absorbs a chorus's wide word,
cheaply.

**Flags persist and resolve exactly once.** A resolved line is never
re-flagged. An unresolved flag carries forward across drafts — and a
line that stays flagged and unanswered for draft after draft is itself
the detector's strongest signal. Avoidance is rarely the abstract line
that was written; it's the abstract line the artist keeps declining to
look at.

**Resolution**, one of two ways per flag:

1. **Answer it in the song** — the abstraction gives way to the concrete
   thing, in the artist's words.
2. **Mark it deliberate** — the wide word stays, as a recorded choice.

**Keeping "deliberate" honest.** Marking a line deliberate still
requires answering the question — privately. One sentence in the song's
folder, not the lyric, naming the concrete thing behind the wide word.
Choice can answer the question and declines to put the answer in the
song; avoidance can't answer it. A chorus that needs "empty" survives
this in ten seconds; a line that's hiding something will make that one
private sentence feel strangely hard — and that difficulty is the
detector working. A whole section may be marked deliberate as a unit
(one private answer for the section), and section-level marks are
counted distinctly. All deliberate marks are counted per song as a
process statistic: a song where most flags resolved to "deliberate" is
visible as such.
