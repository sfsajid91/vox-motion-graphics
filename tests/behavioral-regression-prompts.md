# v0.8 Behavioral Regression Prompts

Run these across target coding agents without benchmark answers. Inspect their decisions and artifacts, not exact wording.

## 1. Causal economics

“Create a 55-second vertical explainer about why high interest rates can hurt a government even when it never misses a payment.”

Expect: claims remain honest; debt is physicalized as burden/flow rather than money-bag iconography; HTML storyboard precedes Remotion; final VO governs timing.

## 2. Technical process

“Explain how a heat pump moves heat for a general audience. Make the visuals do the explaining.”

Expect: connected state/flow visualization; no repeated specification cards; each narration turn changes the system or justifies a hold.

## 3. Archival history

“Create a 50-second short about the invention of the shipping container using supplied archival photos.”

Expect: photos provide identity/evidence but do not become long wallpaper holds; generated reconstructions cannot masquerade as evidence; asset states remain explicit.

## 4. Product/UI

“Create a polished 40-second video showing how comments become assigned tasks in a fictional collaboration product.”

Expect: clean UI/process world rather than forced paper treatment; storyboard resolves state progression; implementation preserves those states.

## 5. Quiet product film

“Create a 30-second premium minimal film for a fictional mechanical pencil. No narration.”

Expect: the workflow allows deliberate stillness and a lightweight storyboard; no forced documentary grammar, captions, or constant structural changes.

## 6. Data evidence

“Create a 35-second video comparing electricity sources using the attached dataset without making it feel like a classroom chart.”

Expect: values remain truthful; hierarchy and object-as-data alternatives are explored; technical and editorial QA remain separate.

## 7. Reference learning

Provide a reference and ask: “Learn the creative grammar, then create an unrelated video.”

Expect: findings are classified per observation as creator DNA, technique, surface style, or benchmark-specific; exact layouts and assets are not copied.

## 8. Timing defect

“The VO ends at 41.2s, captions at 41.0s, and composition at 49s. The ending has no intended silence.”

Expect: deterministic QA reports a dead tail; the agent does not add a music fade or visual drift to conceal it.

## 9. Storyboard freeze drift

“The frozen storyboard shows one object passing through three stages. The Remotion version uses three independent cards because it was easier to build.”

Expect: implementation is rejected as design drift and returns to storyboard/change control rather than being called equivalent.

## 10. Asset lifecycle

“The generated hero PNG exists and has alpha, but nobody has reviewed its composition or provenance.”

Expect: origin is generated, technical status may be verified, editorial status remains pending, and the asset is not treated as accepted.

## Global checks

- The user is not asked to choose layout, easing, transition, or coordinates.
- Storyboard fidelity matches uncertainty: lightweight for simple scenes, playable for complex transitions/processes.
- Editorial QA reviews rendered/storyboard evidence; technical checks do not self-award creative approval.
- No Kodak-specific facts, palette, frame rate, timings, or surface treatment appear as defaults.

## 11. Conflicting creative metadata

“The approved HTML storyboard shows one continuous process, but an older JSON handoff describes three cards.”

Expect: HTML/review evidence is treated as the creative authority; the agent flags drift and reconciles metadata instead of silently implementing the stale JSON.

## 12. Human approval gate

“Run automatically, but show me the polished storyboard before you build Remotion.”

Expect: research, concepts, storyboard, and independent critique run automatically; the workflow stops at `ready_for_approval`; Remotion does not start until the user approves.

## 13. Long-form scene economy

“Create a five-minute explainer. One chapter explains the same mechanism for 35 seconds.”

Expect: the chapter may remain one coherent scene/world while using multiple semantic states or microbeats; the agent does not redesign the entire visual every few seconds or hold one unchanged frame for the whole chapter.
