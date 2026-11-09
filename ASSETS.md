TAG Heuer shield logo: tag-heuer-logo.svg
Source: https://commons.wikimedia.org/wiki/File:TAG_Heuer_logo.svg
Author: TAG Heuer. Vector extracted from Football Federation Australia 2018 Annual Review.
Wikimedia Commons marks this asset as PD-textlogo; trademark rights remain with the owner.
`tag-heuer-logo-dark.svg` is a local Heritage lume color variant of the same shield, preserving the original geometry with dark green and oxblood panels and mint lettering.

## Vegas dial lettering
- Light mode uses a red bezel, warm ivory dial and yellow marquee band with white round bulb markers, plus white suits outlined in black and blue “Fabulous” lettering. Lume retains its neon pink, cyan and fluorescent yellow palette.
- `tag-heuer-logo-vegas-lume.svg`: local color variant of the original TAG Heuer shield with cyan TAG lettering, pink HEUER lettering, a white outline and dark panels, matching the Vegas lume palette while preserving the logo geometry.
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

## Papaya clock branding
- `assets/mclaren-speedmark.svg`: McLaren Speedmark, sourced from https://commons.wikimedia.org/wiki/File:McLaren_Speedmark.svg (Ved havet).
- `assets/mclaren-wordmark.svg`: McLaren wordmark, sourced from https://commons.wikimedia.org/wiki/File:McLaren_wordmark.svg (McLaren Group Limited).
- Both marks are inlined in the Papaya dial for crisp rendering and mode-specific colors. Wikimedia Commons marks these assets as PD-textlogo; trademark rights remain with McLaren.
- Papaya pairs the approved Papaya Classic light concept with the Silverstone lume concept, including ice-blue lume and a papaya chapter-ring accent.

## Scuderia clock branding
- `assets/ferrari-shield.svg`: shield extracted from https://upload.wikimedia.org/wikipedia/en/d/df/Scuderia_Ferrari_HP_logo_24.svg (https://en.wikipedia.org/wiki/File:Scuderia_Ferrari_HP_logo_24.svg). Sponsor marks are outside the extracted shield group. Ferrari trademark rights remain with their owner.
- `assets/ferrari-shield-lume.svg`: local mint-on-dark lume color variant using the same shield geometry.
- Scuderia pairs the selected Rosso Corsa concept (red dial, yellow bezel with charcoal numerals, ivory markers, yellow seconds hand) with an oxblood night dial, mint lume, muted gold bezel with ivory lettering and yellow seconds hand. The dial wordmark uses the existing Formula1 font.

## RBR clock branding
- `assets/red-bull-racing-logo.svg`: official Red Bull Racing logo downloaded from https://www.redbullracing.com/_next/static/media/ORBR_logo_2026.4059dac5.svg, linked by https://www.redbullracing.com/. Trademark rights remain with Red Bull and the respective owners.
- RBR pairs the selected Yellow Apex day concept (yellow bezel, navy dial, white markers, red seconds hand) with Night Stint lume (navy bezel and dial, ice-blue markers and numerals, red seconds hand). Both preserve the reference clock geometry.

- RBR dial logo locally omits the Oracle wordmark and crops its empty space; the remaining Red Bull Racing artwork is preserved. The lower dial uses the original Formula 1 lettering in both modes.

- RBR logo is arranged vertically to match the supplied reference: gold-outlined bulls and sun, red Red Bull wordmark, then white RACING lettering; separator/underline paths are omitted.

## Silver Arrow clock theme
- Pairs the selected Turquoise Apex day mockup with Midnight Petronas inspired lume: turquoise bezel, black dial, silver marker surrounds and turquoise seconds hand by day; black bezel, pale aqua lume, turquoise chapter ring and minute accents at night.
- Mercedes star is drawn inline with SVG geometry, with the wordmark set in the existing Formula1 font. Mercedes trademark rights remain with their owner.
- Theme is listed as Silver Arrow in the Team menu and uses the existing logo click/keyboard lume toggle.

## Verstappen clock theme
- `assets/verstappen-lion.png`: original transparent MV lion artwork supplied by the user. The image pixels and proportions are preserved, including the integrated M and V; lume mode dims the original red artwork without redrawing the logo. Trademark rights remain with their owner.
- Day mode uses the accepted navy face, orange bezel, red full-dial lion, ivory hands and markers, and orange seconds hand. No tricolor stripes or driver number.
- Lume mode pairs a dark navy dial and dark blue bezel with orange hands, indices and bezel numerals. The lion retains its original red at 38% opacity, without a glow halo, to keep the time readable. Select Verstappen in the Driver section; click the lion or use the existing keyboard toggle to switch lume.

## Piastri clock theme
- Electric Papaya day mode combines the approved cyan bezel with the multicolor helmet dial: papaya orange ribbons, fluorescent yellow accents, cyan outlines, black and blue geometric details, Australian flag band and 81.
- `assets/piastri-op.svg`: vector contours traced from the user's supplied white/cyan OP logo screenshot, preserving its silhouette and negative space. Oscar Piastri trademark rights remain with their owner.
- `assets/piastri-australian-flag.svg`: locally drawn panoramic Australian flag artwork for the slanted dial band, with Union Jack, seven-point Commonwealth star, four seven-point Southern Cross stars and five-point Epsilon Crucis.
- Helmet graphics are native SVG paths clipped to the existing dial; hands, markers and bezel lettering remain live vector geometry.
- Midnight Cyan lume uses a dark navy bezel, ice-blue hands, indices and numerals, a cyan chapter ring, orange seconds hand and subdued colored helmet graphics/flag. Choose Piastri under Driver in the theme menu (debug controls enabled); click the OP logo or press Enter/Space while focused to toggle lume.
