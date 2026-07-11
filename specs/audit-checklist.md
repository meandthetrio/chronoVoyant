# Audit Checklist

Run against any draft on request ("audit this against the spec").
The output is a list of drift findings, not opinions. Per The Bible:
never ask "is this good?" — ask for this audit instead.

## Spec conformance

- [ ] POV consistent in every line (flag each drift with line number)
- [ ] Tense consistent in every line (flag each drift)
- [ ] Setting maintained — does any section float free of the declared
      time/place?
- [ ] Structure matches the declared form map
- [ ] Hook arrives by the declared point
- [ ] Every song-specific non-negotiable checked, one by one

## Intent match

- [ ] Read the draft cold, state what it appears to be about in one
      sentence, and compare to the spec's Intent line. If they differ,
      say so plainly: "You set out to write about X; this draft is
      about Y — which is it?"

## Deviations

- [ ] Every violation found: is it in `deviation-log.md` as deliberate?
      If not, it's drift and gets flagged.

## Output format

```
AUDIT: <song> — <draft file> — <date>
CONFORMS: <count> checks passed
DRIFT: <line/section>: <rule broken>: <what the text says vs. spec>
INTENT: match | mismatch (<cold read> vs. <declared>)
UNDECLARED DEVIATIONS: <list or none>
```
