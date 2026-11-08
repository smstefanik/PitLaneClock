TAG Heuer shield logo: tag-heuer-logo.svg
Source: https://commons.wikimedia.org/wiki/File:TAG_Heuer_logo.svg
Author: TAG Heuer. Vector extracted from Football Federation Australia 2018 Annual Review.
Wikimedia Commons marks this asset as PD-textlogo; trademark rights remain with the owner.
`tag-heuer-logo-dark.svg` is a local Heritage lume color variant of the same shield, preserving the original geometry with dark green and oxblood panels and mint lettering.

## Vegas dial lettering
- `#vegas-lettering` in `index.html`: outlined “Fabulous” (Brush Script MT) and “LAS VEGAS” (Arial Black), generated with Core Text from locally installed macOS fonts. The SVG outlines render consistently without loading or distributing font files. Arrangement and light/dark colors follow the user-supplied Vegas references.

## Race heading
- `assets/fonts/Michroma-Regular.ttf`: Michroma by Vernon Adams, from https://github.com/google/fonts/tree/main/ofl/michroma. SIL Open Font License included alongside the font.
- `assets/brazil.svg`: full 10:7 Brazil flag from https://flagcdn.com/br.svg (Flagpedia / FlagCDN). Replaces the cropped 4:3 variant.
- `assets/mexico.svg`: flat Mexico flag from https://github.com/lipis/flag-icons. MIT license in `assets/LICENSE-flag-icons.txt`.

## Formula 1 typography
- `assets/fonts/Formula1-Regular.woff2` and `Formula1-Bold.woff2` downloaded from https://www.formula1.com/s/fonts/formula1/ as requested. The Mexico race page uses Formula1 weight 400 for its race heading and weight 500 (Bold file) for session titles, defined in https://www.formula1.com/s/fonts.css. These are proprietary Formula 1 assets; no redistribution license was supplied by the source.

## Formula 1 logo
- `assets/formula-1-logo.svg`: Formula One logo by Liberty Media, from https://commons.wikimedia.org/wiki/File:Formula_One_logo.svg. Wikimedia Commons marks this asset as PD-textlogo; trademark rights remain with the owner.

## Additional race flags
- `assets/united-states.svg`, `assets/qatar.svg`, and `assets/united-arab-emirates.svg`: country flags from https://flagcdn.com/us.svg, https://flagcdn.com/qa.svg, and https://flagcdn.com/ae.svg (Flagpedia / FlagCDN), matching the Brazil flag source.

## Race schedule data
- `races.js`: remaining 2026 F1 weekends, with São Paulo retained for debug previews. Names and F1 session start/end times verified on 2026-11-08 against https://www.formula1.com/en/racing/2026 and each race’s linked full timetable. Exact source URLs are stored with each race.
- Timestamps are UTC; track dates and times use IANA time zones. Race completion uses the published two-hour race slot, not live results. This is a local schedule snapshot; timetable changes require updating the array.
