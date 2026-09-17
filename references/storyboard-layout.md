---
name: Storyboard Layout System
description: Editorial control-room layout for reviewing a vertical storyboard as a repeatable sequence of scenes and inspection modules.
colors:
  paper: "#f4efe5"
  paper-warm: "#ece5d6"
  paper-card: "#faf7f0"
  paper-card-subtle: "#f0eae0"
  ink: "#111923"
  ink-secondary: "#333f4e"
  muted: "#535e6c"
  line: "rgba(17, 25, 35, 0.12)"
  line-strong: "rgba(17, 25, 35, 0.22)"
  navy: "#071423"
  canvas: "#0d141e"
  blue: "#1c5d8f"
  red: "#ba2b1d"
  red-soft: "rgba(186, 43, 29, 0.08)"
  amber: "#d48b28"
  acid: "#889e24"
  white: "#ffffff"
  dark-paper: "#0c1219"
  dark-warm: "#111a24"
  dark-card: "#15202c"
  dark-card-subtle: "#192634"
  dark-ink: "#f8fafc"
  dark-ink-secondary: "#cbd5e1"
  dark-muted: "#94a3b8"
  dark-line: "rgba(240, 244, 248, 0.14)"
  dark-line-strong: "rgba(240, 244, 248, 0.24)"
  dark-pill: "#172230"
  dark-control: "#1c2a3a"
  dark-control-hover: "#25364b"
  dark-active-ink: "#0c1219"
  dark-active-muted: "#475569"
  dark-red: "#f87171"
typography:
  display:
    fontFamily: "Newsreader, Georgia, Times New Roman, serif"
    fontSize: "clamp(44px, 5.5vw, 80px)"
    fontWeight: 400
    lineHeight: 0.96
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Newsreader, Georgia, Times New Roman, serif"
    fontSize: "clamp(28px, 3.2vw, 40px)"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Newsreader, Georgia, Times New Roman, serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: "ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: "11px"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.08em"
rounded:
  sm: "4px"
  md: "8px"
  pill: "999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "20px"
  2xl: "24px"
  3xl: "28px"
  4xl: "32px"
  5xl: "36px"
  6xl: "40px"
  section: "52px"
  page-bottom: "100px"
components:
  navigation-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "10px 16px"
  tool-button:
    backgroundColor: "{colors.paper-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: "44px"
  content-card:
    backgroundColor: "{colors.paper-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "16px 20px"
  vertical-canvas:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    size: "9 / 16"
  frame-card-selected:
    textColor: "{colors.red}"
    rounded: "{rounded.sm}"
    padding: "0"

---

# Design System: Storyboard Layout System

## Overview

**Creative North Star: "Editorial Control Room"**

This is a calm, information-dense review surface for a sequence of visual work. It reads like an editorial desk: a strong masthead establishes the artifact, a sticky director’s rail keeps navigation available, and the body repeats one dependable inspection unit per scene. The page uses a warm paper field, dark ink, compact mono labels, and a restrained red signal so the hierarchy feels authored without becoming a dashboard.

The layout separates overview from inspection. A seven-item contact sheet gives the whole sequence a fast scan; each scene then expands into metadata, editorial context, one focal vertical canvas, a row of supporting inspection cards, and short director notes. The shell is intentionally repeatable. Frame artwork, scene-specific content, and motion behavior are outside this system document.

**Key Characteristics:**
- Centered 1540px editorial frame with generous outer margins.
- Sticky horizontal navigation rail with persistent scene jumps and one utility action.
- Overview-first contact sheet followed by repeatable two-column scene inspection modules.
- Warm layered paper, hairline rules, small radii, and restrained canvas shadows.
- Responsive collapse from desktop inspection pair to a centered single-column mobile flow.

## Colors

The shell uses warm paper neutrals and dark ink, with red reserved for active state and editorial signal. Dark mode swaps the paper and ink roles through `prefers-color-scheme: dark`; the accent relationships remain recognizable.

### Primary
- **Signal Red** (`#ba2b1d`): Active scene state, selected frame outline, locked cue marker, and the small visual signal that tells the reviewer where attention belongs.

### Secondary
- **Technical Blue** (`#1c5d8f`): Cool supporting accent used in the visual language and atmospheric background treatment; keep it subordinate to the red signal.
- **Instrument Amber** (`#d48b28`): Safe-zone and measurement cue accent; use sparingly for technical overlays and secondary emphasis.

### Tertiary
- **Acid Olive** (`#889e24`): Rare secondary status accent for contrast inside visual work; never let it compete with the primary signal.

### Neutral
- **Paper** (`#f4efe5`): Primary light-mode page field.
- **Warm Paper** (`#ece5d6`): Scrollbar track and supporting warm surface.
- **Card Paper** (`#faf7f0`): Content cards, controls, and narration surfaces lifted one level from the page.
- **Subtle Card Paper** (`#f0eae0`): Available for low-priority card variation; do not introduce it without a clear hierarchy need.
- **Ink** (`#111923`): Primary text and active navigation fill.
- **Secondary Ink** (`#333f4e`): Supporting copy, theses, and explanatory text.
- **Muted Ink** (`#535e6c`): Metadata, timestamps, and low-emphasis labels.
- **Hairline** (`rgba(17, 25, 35, 0.12)`): Quiet separators and section label rules.
- **Strong Hairline** (`rgba(17, 25, 35, 0.22)`): Structural boundaries between masthead, overview, and scenes.
- **Canvas** (`#0d141e`): Neutral backing behind vertical visual canvases and thumbnails.
- **White** (`#ffffff`): Text placed on dark active controls and canvas overlays.
- **Dark Paper** (`#0c1219`), **Dark Warm** (`#111a24`), **Dark Card** (`#15202c`), and **Dark Ink** (`#f8fafc`): Dark-mode surface and text roles.

### Named Rules
**The Signal Scarcity Rule.** Red is a locator, not a wash: reserve it for active, selected, locked, or consequential states.

## Typography

**Display Font:** Newsreader (with Georgia, Times New Roman, serif fallbacks)
**Body Font:** ui-sans-serif system stack (with system UI fallbacks)
**Label/Mono Font:** JetBrains Mono (with ui-monospace fallbacks)

**Character:** Newsreader supplies an editorial voice with compact, high-contrast headlines. System sans keeps explanatory copy legible, while JetBrains Mono turns timings, statuses, and navigation indices into production metadata.

### Hierarchy
- **Display** (400, `clamp(44px, 5.5vw, 80px)`, 0.96): The masthead title; keep the title block capped at 980px.
- **Headline** (400, `clamp(28px, 3.2vw, 40px)`, 1.08): Scene titles inside the repeated inspection shell.
- **Title** (400 italic, 17px, 1.4): Short scene thesis or editorial framing line beneath a scene title.
- **Body** (400, 16px, 1.5): Masthead description and readable explanatory copy.
- **Label** (700, 11px, 1.4, `0.08em`, uppercase): Navigation indices, section labels, statuses, timing, and production metadata.

### Named Rules
**The Two-Register Rule.** Use serif for editorial statements and system sans/mono for operational metadata; do not make every label compete with the headline voice.

## Layout

Use one centered page frame: `max-width: 1540px; margin: 0 auto`. On desktop, the masthead and director rail share the same frame width. The masthead uses a `1fr auto` grid with a 32px gap and bottom alignment. Its light-mode padding is `52px 40px 32px`; at `max-width: 860px` it becomes `40px 24px 24px` and stacks into one column.

The sticky director rail sits at the top of the viewport (`top: 0`) with a translucent paper surface, 14px backdrop blur, a bottom rule, and a 100px stacking level. Its inner row uses `10px 40px` padding, keeps scene jumps in a horizontally scrollable group, and holds utility actions on the opposite edge. At `max-width: 860px`, horizontal padding becomes 24px. At `max-width: 580px`, hide the director tools and keep the jump buttons compact.

The main frame uses `padding: 40px 40px 100px`. The contact sheet comes first with `48px` bottom margin, `32px` bottom padding, and a strong bottom rule. Its seven equal columns use a 14px gap. At `max-width: 1080px`, use four columns. At `max-width: 680px`, switch to a horizontal scroll row with 130px minimum cards so the overview remains a single gesture rather than a cramped miniature grid.

Each scene is a repeated article shell: a 140px metadata rail plus a flexible body separated by 36px, with `52px 0` vertical padding and a structural bottom rule. The metadata rail sticks below the navigation at `top: 76px`. The scene body begins with a title/status row, a short thesis, and a content card, then moves into the inspection pair. At `max-width: 860px`, scenes become one column with 20px gaps and 40px vertical padding; metadata becomes a static horizontal row and the progress pip disappears.

The inspection pair is `.canvas-row`: `minmax(300px, 350px) minmax(0, 1fr)` with a 32px gap. The left column is the focal stage; the right column is the sequence inspection area. At `max-width: 1180px`, use `minmax(260px, 320px) minmax(0, 1fr)` and 24px gap. At `max-width: 860px`, stack the pair, center the focal stage, and cap the focal canvas at 360px wide. The sequence grid is four columns with 12px gaps on wide screens and two columns below 1180px; below 580px it becomes one column.

Director notes close each scene body as a two-column grid with a 28px gap, separated from the inspection pair by a top rule. Below 680px, stack note columns with a 16px gap. Preserve this order when replicating: page frame → masthead → sticky rail → contact sheet → scene shell → scene context → focal/sequence pair → notes.

### Named Rules
**The Overview-Then-Inspect Rule.** Always give the reviewer a compact whole-sequence scan before the detailed scene modules.

**The Stable Scene Unit Rule.** Every scene must keep the same outer anatomy even when its internal visual content changes.

## Elevation & Depth

This is layered paper, not a floating-card dashboard. Depth comes first from surface shifts and structural rules, then from small shadows on controls and canvases. The page remains mostly flat; shadows should clarify a tactile inspection surface without pulling attention away from the visual work.

### Shadow Vocabulary
- **Card lift** (`0 2px 6px rgba(17, 25, 35, 0.06)`): Narration cards and compact controls on the light paper field.
- **Canvas lift** (`0 4px 12px rgba(7, 20, 35, 0.16)`): Vertical canvases and thumbnails against the paper field.
- **Medium lift** (`0 8px 18px rgba(17, 25, 35, 0.1)`): Reserved for an explicitly elevated state, not default containers.
- **Dark card lift** (`0 2px 6px rgba(0, 0, 0, 0.4)`): Dark-mode compact surfaces.

### Named Rules
**The Layered Paper Rule.** Use a surface or rule to establish hierarchy before increasing shadow strength.

## Shapes

The form language is crisp and editorial. Most containers use a restrained 4px radius; 8px is available for a larger secondary shape, while scene jump navigation is the one intentionally pill-shaped control (`999px`). Borders are 1px hairlines, with 2px red outlines reserved for a selected frame. Vertical canvases and thumbnails clip their contents with `overflow: hidden` and keep a 9:16 aspect ratio.

Interactive targets stay generous even when labels are small: scene jumps, tools, scene controls, and beat buttons use a minimum 44px height. Avoid excessive rounding, nested pills, and heavy card chrome.

## Components

### Masthead
- **Shape:** Full-width page-frame header with a strong bottom rule; no card shell.
- **Layout:** Two-column title/meta grid, 32px gap, bottom aligned; stack below 860px.
- **Type:** Newsreader display title plus system-sans description; metadata uses mono.
- **Meta treatment:** One dark pill for the artifact format, followed by a compact mono spec line.

### Director Navigation Rail
- **Shape:** Sticky, full-width translucent band with a 1px bottom rule.
- **Layout:** Horizontally scrollable scene jump group on the left; utility action group on the right.
- **States:** Inactive jumps are transparent; active jump is dark ink with white text; tools use card paper and a 4px radius.
- **Responsive:** Rail remains scrollable; utility tools disappear below 580px.

### Contact Sheet
- **Shape:** Borderless overview section separated by a strong bottom rule.
- **Layout:** Seven equal thumbnail columns with 14px gaps; four columns at 1080px; horizontal 130px cards at 680px.
- **Caption:** Scene identifier first, mono time range second; captions never become a dense paragraph.
- **Behavior:** Each card is a jump target and may lift 3px on hover; do not add a second action inside the card.

### Scene Shell
- **Shape:** Repeated article section with a bottom rule and generous vertical padding.
- **Layout:** Sticky metadata rail plus flexible body; metadata collapses to a horizontal row below 860px.
- **Header:** Scene title and status share a wrapping baseline row; thesis follows; the narration card sits before the inspection pair.
- **Density:** Keep the outer rhythm constant; vary only the scene’s internal content.

### Narration Card
- **Shape:** Card paper, 1px strong hairline, 4px radius, small lift.
- **Layout:** Compact header row for cue tag and stats, followed by a serif text block.
- **Padding:** `16px 20px`; 24px bottom separation before the inspection pair.
- **Signal:** Red cue label and dot; metadata remains muted.

### Inspection Pair
- **Shape:** No outer card; the page grid provides the grouping.
- **Layout:** 350px focal stage beside a flexible sequence area, 32px gap; stack and center below 860px.
- **Subsections:** Both columns start with the same section-label bar: mono label, optional icon, muted sublabel, bottom rule.

### Vertical Canvas
- **Shape:** 9:16 aspect ratio, 4px radius, clipped content, 1px dark border, canvas shadow.
- **Overlay:** Small top-left HUD and bottom-left frame mark are informational overlays; keep them inside the canvas boundary.
- **Responsive:** Focal canvas is fluid on desktop and capped at 360px when stacked.

### Frame Card
- **Shape:** Borderless inspection unit with an internal header rule; canvas supplies the visual container.
- **Layout:** Timing row, action label, 9:16 canvas, then a two-line-clamped note; use 12px vertical gaps.
- **States:** Hover lifts 2px and strengthens the canvas border. Selected state uses a red border, 2px outline, and stronger shadow.
- **Interaction:** Whole card is the inspection target; preserve keyboard focus visibility.

### Director Notes
- **Shape:** Borderless two-column closeout with a top rule.
- **Layout:** Two note columns at 28px gap; one column below 680px.
- **Type:** Mono uppercase headings; 13px system-sans body copy with 1.48 line-height.

## Do's and Don'ts

### Do:
- **Do** keep every top-level region inside the shared 1540px centered frame.
- **Do** preserve the order: masthead, sticky rail, overview, repeated scenes, notes.
- **Do** keep scene metadata visually separate from the scene body with a stable 140px rail on desktop.
- **Do** use the focal/sequence split to make one primary inspection surface and one supporting sequence legible at once.
- **Do** preserve 9:16 canvases and 44px interaction targets when adapting the layout.
- **Do** use hairline rules and surface shifts before adding more shadow.
- **Do** let mobile become a clean single-column flow instead of shrinking the desktop composition.

### Don't:
- **Don't** redesign the shell around frame art, scene content, or motion behavior; those are separate concerns.
- **Don't** replace the overview contact sheet with a generic hero or dashboard summary.
- **Don't** bury scene navigation inside the page body; the director rail is intentionally sticky.
- **Don't** use a masonry grid, arbitrary card heights, or inconsistent scene anatomy.
- **Don't** turn every label into a pill or every surface into a floating card.
- **Don't** remove the horizontal overflow behavior that keeps navigation and mobile overviews usable.
- **Don't** promote accent colors to large backgrounds; red, amber, and olive are signals.
