# Motion Choreography & Camera Grammar v0.6

## Principle
Motion is choreography of meaning. The question is not “what animation looks cool?” but “what changes when this word/idea lands?”

## Motion Stack Per Scene
A strong scene usually contains:
1. **primary semantic motion** — the event that explains the beat;
2. **supporting motion** — 1–2 actions that clarify hierarchy or consequence;
3. **camera behavior** — only if it reveals/reframes/transitions;
4. **ambient life** — subtle drift, boil, light, focus, particles, route pulses, etc.;
5. **settle/hold** — intentional breathing room;
6. **handoff** — object, gaze, direction or scale launch into the next scene.

Do not animate all layers simultaneously.

## Semantic Timing
Use narration alignment, not guessed frame numbers, for final choreography.

Attach motion to spoken anchors:
- noun appears / object established;
- verb triggers action;
- contrast word introduces counter-state;
- number/stat locks into evidence state;
- reversal causes camera or composition pivot;
- payoff receives a settle/hold rather than another transition.

For short narrated sequences, the first readable visual state should normally follow the order in which semantic anchors are introduced. If the line moves `date -> person/place -> evidence object`, establish those beats in that order unless a deliberate reveal needs temporary concealment.

## Adding a Beat to an Existing Scene
When a scene already has a strong settled composition and a new semantic beat is introduced:
1. identify where the new idea occurs in the narration;
2. preserve the accepted composition long enough to read;
3. prepend/re-time when the new idea is the opening spoken anchor;
4. extend the scene when the new idea follows the existing payoff and narration has room;
5. redesign the composition only when the new beat changes the scene's actual thesis.

Do not solve added meaning by simply stacking another hero object over the existing focal subject. Give the new object its own evidence state and handoff.

## Motion Personality
Choose a small motion vocabulary that fits the material world:
- mechanical / ratcheted;
- elastic / springy;
- editorial / stepped;
- frictionless digital;
- heavy inertial;
- archival / restrained;
- anxious / unstable;
- elegant / premium.

Posterized motion, gate weave and boil are optional treatments, not defaults.

## Repeated Objects
Never clone entrances mechanically unless uniformity itself is the point.
Vary:
- direction;
- rotation;
- entry delay;
- distance;
- scale;
- settle stiffness;
- z-depth.

Repeated props should feel choreographed, not looped.

## Camera Grammar
Use the camera for information:
- push in to inspect/reveal;
- pull out to expose scale/system/consequence;
- lateral travel to connect process/timeline/geography;
- portal to transform one meaningful object into the next world;
- punch-in to intensify hierarchy;
- focus hunt to simulate inspection/search;
- orbit/parallax only when depth relationships matter.

Remove camera drift that discovers nothing.

## Attention Continuity
The camera and object motion should support planned entry/exit focal zones.

Useful handoffs:
- object exits right -> next scene action enters from right;
- line/path persists across the cut;
- camera dives into screen -> next world originates inside the screen;
- macro close-up -> next scene expands to systemic wide view;
- focal object contracts into a map node/document marker in the next scene.

## 2.5D Rigs from the Reference Corpus
These are optional reusable mechanics:

### Weld-and-Detach Portal
Move frame/photo/screen as one object, then detach layers during a push-through so the foreground frame accelerates past the lens while the image/environment becomes the next scene.

### Differential Depth Punch
Move foreground and background at different scale rates. Add believable contact/floor shadow or occlusion to ground the foreground layer.

### Grounded Shadow
Duplicate/silhouette a cutout, transform it onto the floor plane, darken/blur it, and bind its origin to the subject’s feet/base.

### Swinging Prop / Light
Use damped or sinusoidal rotation on the prop while a separate light cone/spill follows the same pivot. The light must affect the scene, not exist as decoration.

### Staggered Cascade
Documents/cards/photos arrive from varied trajectories and rotations. Their order should follow narration semantics.

### Damped Gesture
For wagging hands/pointers/needles, use oscillation with decay so the action resolves instead of looping forever.

### Hold-Keyframe Flicker
For neon/cash/light emphasis, use stepped state changes or deterministic flicker when smooth opacity fades would feel wrong.

## Ambient Life
Use sparingly:
- 0.2–1% scale breathing;
- tiny rotation/translation;
- subtle route particles;
- light sweep;
- focus drift;
- print-registration jitter;
- deterministic grain;
- character boil.

Ambient motion must never compete with the primary semantic action.

## Rig Reuse
Reusable mechanics may become semantic primitives:
`CameraRig`, `LayeredCutout`, `GroundedShadow`, `ObjectPortal`, `PropCascade`, `LightCone`, `FocusHunt`, `PosterizeMotion`, `NetworkFlow`, `CountUp`, `PathDraw`, `HoldFlicker`, `DampedGesture`.

Reskin them per story. Never expose the viewer to obvious scene templates.
