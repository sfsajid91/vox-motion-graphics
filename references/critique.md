# Editorial and Technical Critique

## Two Independent Questions

A video may render perfectly and still be visually weak. It may also have a strong storyboard and fail technically.

Keep two explicit verdicts:

- **editorial verdict**: does the visual storytelling work?
- **technical verdict**: is the implementation correct, complete, and safe to render?

Neither verdict substitutes for the other. A publish candidate requires both to pass.

## Verdict Ownership

The agent that creates or implements an artifact may identify risks and request review, but it must not approve its own work or assign itself a production-ready status.

Use an independent critic, reviewer agent, or explicit human review. Independence means a separate review pass that receives the artifact and criteria without being asked to defend the generator's prior choices. Prefer a human or separate agent/model context; a clean critic context on the same model is acceptable when stronger separation is unavailable.

The critic must inspect the artifact itself:

- storyboard review uses the HTML preview and representative states;
- render review uses actual frames and motion previews;
- technical review uses the implementation, timing data, asset ledger, and validation output.

If no independent reviewer is available, mark the relevant verdict `unreviewed`. Continue only as a draft; do not claim approval or production readiness. If the user explicitly owns the approval gate, the critic may mark work `ready_for_approval` but only the user's approval freezes it.

## Editorial QA

Editorial QA asks whether the film communicates with clarity, specificity, and deliberate visual direction.

### Review dimensions

- **Visual thesis:** can the scene's main relationship or state change be described without repeating the narration?
- **Focal hierarchy:** is one element dominant in each meaningful state, and does attention move intentionally?
- **Mechanism clarity:** does the scene show cause, process, comparison, transformation, or evidence rather than merely illustrate nouns?
- **State progression:** does visual structure evolve when the narration introduces a new idea?
- **Payoff:** does the scene land on a readable consequence, often with a simpler composition than the buildup?
- **Pacing:** are holds purposeful, actions readable, and transitions timed around semantic resolution?
- **Continuity:** does attention hand off through position, direction, object, line, color, or scale?
- **Asset fitness:** do the selected assets support the required crop, motion, identity, and tone?
- **Text restraint:** is text limited to labels, evidence, short emphasis, or accessibility rather than duplicating the voiceover?
- **Style cohesion:** do continuity tokens create one film without forcing every scene into the same layout?
- **Evidence honesty:** are literal, evidence, reconstruction, metaphor, and abstract treatments unmistakable and claim-safe?

### Editorial verdicts

- `approve`: visual decisions are ready to freeze or publish at this stage;
- `revise`: the concept works but named issues require repair;
- `redesign`: the mechanism, hierarchy, or representation is fundamentally weak;
- `unreviewed`: no independent editorial review occurred.

Every non-approval verdict should name the symptom, affected scene/state, responsible design decision, and smallest useful repair.

## Technical QA

Technical QA asks whether the accepted design has been implemented deterministically and without delivery defects.

### Review dimensions

- composition renders at the declared size, frame rate, and duration;
- scene, narration, caption, transition, and final-hold timing reconcile;
- no dead tail or early cut remains unexplained;
- render-visible motion is frame-driven and deterministic;
- assets load reliably and use supported formats/paths;
- required provenance, rights, and claim references exist;
- text and critical subjects remain inside the named platform safe area;
- captions fit, remain legible, and do not collide with critical art;
- masks, overlays, textures, and transforms preserve intended geometry;
- all expected data, labels, and final values remain visible at settle;
- audio files, channels, sync points, and final mix are present and valid;
- no runtime, typecheck, lint, schema, or render errors remain;
- representative output matches the frozen storyboard or records an approved deviation.

### Technical verdicts

- `pass`: delivery checks are satisfied;
- `fail`: a blocking defect exists;
- `blocked`: required input, tool, credential, or evidence is unavailable;
- `unreviewed`: no independent technical review occurred.

Do not convert technical success into an editorial approval. “It renders” is not evidence that the film communicates well.

## Stage-Specific Review

### Storyboard gate

Run editorial QA only. Technical notes may flag feasibility, but they should not overrule a strong concept until the implementation risk is real and specific.

### Implementation gate

Run technical QA first so broken output does not waste editorial review. Then compare representative renders with the frozen storyboard.

### Final gate

Run both verdicts on the mastered output. Reopen only the responsible layer:

- weak thesis, hierarchy, state change, asset choice, or pacing -> storyboard/editorial repair;
- timing arithmetic, clipping, loading, determinism, captions, provenance, or render failure -> technical repair;
- implementation drift that changes meaning -> storyboard change control, then both reviews again.

## Critique Evidence

Use the smallest evidence set that proves the verdict:

- entry, meaningful action, payoff, and exit frames;
- short motion previews for pacing, camera, or transition issues;
- reduced-size preview for hierarchy/readability;
- narration/caption/scene timing table for duration issues;
- before/after comparison for repairs;
- frozen storyboard comparison for implementation fidelity.

A final frame cannot prove motion quality, and source code cannot prove rendered composition.

## Repair Discipline

Repair in causal order:

1. truthfulness and representation;
2. scene mechanism and visual thesis;
3. focal hierarchy and state progression;
4. asset selection and composition;
5. timing and transition intent;
6. surface treatment and polish;
7. implementation defects within the accepted design.

After two failed low-level repairs to the same editorial problem, return to the storyboard and redesign. If one redesign still cannot produce a clearly better direction, escalate the smallest meaningful choice instead of looping. Do not stack effects or parameters around a weak concept.

