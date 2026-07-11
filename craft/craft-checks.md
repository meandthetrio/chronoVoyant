# Craft Checks

The standard diagnostic pass, run on request against any draft.
Each check reports findings with line numbers. No verdicts, no praise.

## Prosody

- Mark the natural spoken stress of each line. Flag lines where a
  stressed syllable would land on a weak beat (or an unstressed one on a
  strong beat) given the declared groove.
- Flag lines whose syllable count differs from the matching line in a
  parallel section (V1 line 1 vs. V2 line 1) — melody carriers should
  match unless deliberately varied.

## Rhyme

- Map the rhyme scheme per section. Flag scheme breaks between parallel
  sections.
- Flag rhyme-driven lines: lines whose content exists only to reach the
  rhyme. (Tell: the line adds no scene, no information, no turn.)

## Repetition and structure

- Count hook occurrences and note their timestamps/positions.
- Section proportions: flag any verse/bridge that is much longer than
  its parallel sections without a declared reason.
- Flag identical rhythmic openings on consecutive lines (unintentional
  monotony) unless the spec declares it as a device.

## Harmony / arrangement (when charts or audio notes exist)

- Confirm key and mode against the spec.
- Flag chord-function surprises (borrowed chords, deceptive cadences) —
  not as errors, but so they're known and chosen.

## Language

- Flag clichés and stock phrases (any line you've heard in another song).
- Flag abstraction: lines that name a feeling rather than show a scene.
  These get escalated to the `truth/` test — abstraction is where
  avoidance hides.
