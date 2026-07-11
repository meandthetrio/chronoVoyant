# specs/ — Everything Declarative

> "In songwriting the equivalent is holding your *declared intent* against
> the artifact." — The Bible

This folder holds the machinery of declared intent: the spec template,
the audit checklist, and the deviation log.

**Individual song specs do NOT live here.** Each song's spec lives with
the song, at `songs/<title>/spec.md`, so intent is never separated from
the thing it governs. This folder is the toolshed, not the field.

## How it works

1. When a song starts, copy `song-spec-template.md` into its folder and
   fill it in. A spec is declared *early*, while intent is still clean.
2. Every draft committed gets audited against its spec using
   `audit-checklist.md`. Claude runs this with zero fatigue and zero
   politeness.
3. Breaking your own spec is allowed — as a choice. Record it in
   `deviation-log.md` so rule-breaking stays artistic, never accidental.
