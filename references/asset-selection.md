# Asset Selection and Lifecycle

Use this reference when sourcing, generating, reconstructing, approving, or replacing media.

## Route by semantic need

Prefer:

`reuse -> programmatic -> source real/licensed -> reconstruction -> generate`

- **Reuse** an accepted master asset when continuity benefits.
- **Programmatic** graphics suit charts, maps, routes, interfaces, diagrams, labels, simple devices, shadows, and light.
- **Source real/licensed** media when historical identity, documentary evidence, or exact product appearance matters.
- **Reconstruct** when the mechanism matters but exact source appearance does not, or when a neutral approximation is safer than false specificity.
- **Generate** original illustrative subjects, impossible scenes, non-evidence backgrounds, and clearly tracked reconstructions.

Do not replace a failed historical hero asset with a meaningless generic placeholder merely to keep the pipeline moving.

## Orthogonal status model

Track these separately:

### Origin

`reused | programmatic | sourced | reconstructed | generated`

### Technical status

`candidate | available | verified`

Verification covers the declared requirements: file integrity, dimensions, crop, alpha, resolution, motion separability, and other technical checks.

### Editorial status

`pending | accepted | rejected`

Acceptance means the asset is intentionally retained for its scene role. A generated or technically verified asset may remain pending or be rejected.

### Rights status

`unresolved | needs_review | verified | self_created`

Verified rights require source/license evidence. Self-created does not waive factual-representation rules.

### Representation type

`literal | evidence | reconstruction | metaphor | abstract`

Evidence assets require claim references. Generated historical-looking material is a reconstruction, not primary evidence.

## Motion-aware requirements

Before sourcing or generation, record as relevant:

- semantic role and scene usages;
- full-object/full-body need;
- expected crop and maximum zoom;
- minimum dimensions;
- alpha/transparency;
- independent parts;
- viewpoint and rotation tolerance;
- parallax/depth needs;
- whether shadows, text, lighting, and treatment must remain external.

Keep raw assets free of baked subtitles, decorative UI, unnecessary shadows, and irreversible global treatment.

## Candidate policy

Generate/source extra candidates only when the decision is expensive or ambiguous: hero identity, face quality, evidence readability, or difficult composition. Use one candidate for deterministic programmatic support assets unless it fails requirements.

## Acceptance gate

Before implementation, confirm:

- file exists and meets declared technical needs;
- representation and claim linkage are honest;
- provenance/rights state is explicit;
- editorial role is accepted;
- recurring uses point to one master or declared derivatives;
- storyboard uses the same asset identity or explicitly returns for review.

