# Complete Scores — page index for the melody-sync campaign

Source: The Beatles — Complete Scores PDF (1,120 pages, scanned, no text
layer; songs alphabetical, articles ignored, apostrophes sorted
letter-by-letter). Pages are 0-based PDF indices; title pages found by
sparse-page detection + probe reads. `~` = ±1–2 pages, verified when
transcription of that song starts.

| # | Song | Title page (PDF idx) | Status |
|---|---|---|---|
| 1 | All You Need Is Love | 29 | confirmed — TODO |
| 2 | Day Tripper | 166 | **DONE** (DayTripper.xlsx) |
| 3 | Everybody's Got Something to Hide Except Me and My Monkey | 244 | confirmed — TODO |
| 4 | Glass Onion | 312 | confirmed — TODO |
| 5 | A Hard Day's Night | ~349 | pinned by neighbors — TODO |
| 6 | Hello, Goodbye | ~356 | pinned by neighbors — TODO |
| 7 | Help! | ~361 | pinned by neighbors — TODO |
| 8 | I Am the Walrus | 415 | **DONE** (IAmTheWalrus.xlsx) |
| 9 | I Don't Want to Spoil the Party | 427 | confirmed — TODO |
| 10 | I Want to Hold Your Hand | 555 | **DONE** (IWantToHoldYourHand.xlsx) |
| 11 | I'm a Loser | ~464 | pinned (mid-song @466) — TODO |
| 12 | In My Life | 502 | confirmed — TODO |
| 13 | I've Just Seen a Face | ~548 | pinned (I've Got a Feeling @544) — TODO |
| 14 | She Loves You | ~857 | pinned (before She Said, ~861) — TODO |
| 15 | She Said She Said | ~861 | pinned (She's a Woman @867) — TODO |
| 16 | Your Mother Should Know | ~1101 | pinned (mid-song @1104) — TODO |

Also DONE, out-of-list pilot: Across the Universe (AcrossTheUniverse.xlsx).

Calibration anchors seen along the way: And I Love Her 34 · Because 96 ·
A Day in the Life 156 · Everybody's Trying to Be My Baby 248 · Girl ~306 ·
Golden Slumbers 316 · Got to Get You Into My Life ~334 · Honey Pie 408 ·
I Call Your Name ~421 · I'll Follow the Sun ~456 · I Need You ~496 ·
I've Got a Feeling ~541 · I Wanna Be Your Man ~549 · Love You To 630 ·
Run for Your Life 830 · She's a Woman 867 · You've Really Got a Hold on
Me 1110. (Useful for locating any future song by interpolation.)

Workflow per song: verify title page → render vocal-staff crops per
system → transcribe lead (and CHORUS staff where present) → build the
melody-sync workbook (same schema as AcrossTheUniverse.xlsx) →
cross-check key/chords against the Isophonics-derived corpus song file.
