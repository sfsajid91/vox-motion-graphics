# Autonomous Orchestration

Use this reference when the workflow is expected to run with little supervision across research, storyboard, critique, Remotion, audio, QA, and render.

## Default ownership

The director should make ordinary creative decisions without asking the user to choose layouts, easing, transition types, scene count, or coordinates.

Pause only when:

- a factual uncertainty changes the claim;
- rights, brand, identity, or material cost needs user ownership;
- required credentials/assets/tools are unavailable;
- the user explicitly requested an approval gate;
- repeated repair no longer has a clear best next action.

## Stage graph

`brief/research -> story -> concepts -> HTML storyboard -> editorial critic -> repair -> approval/freeze -> final VO -> Remotion -> technical QA -> editorial render QA -> audio/master -> final render`

Keep stage outputs small. The HTML storyboard is the creative source of truth until freeze; Remotion becomes the implementation source after freeze. Machine-readable artifacts should index those decisions, not duplicate them unnecessarily.

## Bounded iteration

Avoid endless agent loops.

For a single editorial problem:

1. identify the symptom and responsible design layer;
2. make the smallest plausible repair;
3. review the changed evidence;
4. if the same problem survives two low-level repair attempts, stop patching and redesign the responsible storyboard decision;
5. if a redesign still cannot produce a clear improvement, escalate to the user with the smallest meaningful choice.

Do not generate many cosmetic variants after a concept is already clearly weaker.

## Approval gates

When the user wants approval before implementation:

- the critic may return `ready_for_approval`;
- show the browser preview plus a concise critic summary;
- do not start final Remotion implementation until approval;
- after approval, freeze the defining visual relationships and treat later redesign as change control.

When the user explicitly delegates approval, an independent critic may freeze the storyboard automatically.

## Critic independence

A useful independent critic is a separate review pass that receives the artifact and evaluation criteria without being instructed to defend the generator's decisions. Prefer, in order:

1. human review;
2. separate model/agent context;
3. same model in a clean critic context with no hidden chain from generation.

A second message in the same implementation context that merely asks “is this good?” is not strong independence.

## Safe parallelism

Parallelize work only after shared decisions are stable.

Good candidates:

- independent research/evidence collection;
- asset sourcing/generation for already-defined roles;
- reusable primitive implementation;
- diagnostic frame extraction;
- independent QA dimensions.

Do not parallelize several agents that can silently redefine the same scene thesis, storyboard, or timing contract. Conflicting proposals remain candidates until one is explicitly retained.

## Resume and interruption safety

Long workflows should be restartable after an interrupted agent session.

Persist only durable stage state, for example:

- current stage;
- approved/frozen storyboard path and revision;
- unresolved blockers;
- accepted asset identities;
- final VO/alignment path;
- last QA verdicts;
- requested next action.

Do not serialize the entire reasoning transcript as production state. On resume, reconstruct context from approved artifacts and concise stage metadata.

## Change control after freeze

Changes that alter the thesis, focal hierarchy, defining relationship, hero/evidence asset identity, or transition logic return to storyboard review.

Changes limited to easing, interpolation, micro-timing, compositing, performance, or bounded layout repair may remain in implementation if they preserve the approved visual argument.

## Completion

A run is complete when:

- requested approval gates have been satisfied;
- factual/rights blockers are resolved or explicitly surfaced;
- implementation matches frozen direction;
- technical QA passes;
- editorial review has a valid verdict;
- requested render/output exists.

Do not continue polishing merely because another effect or variant is possible.
