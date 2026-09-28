# Vague Autopilot Regression Prompts

Use these without extra motion-design guidance. The skill should make creative choices internally and should not ask the user to storyboard.

1. `Make an engaging 50 second short about why Nokia lost the smartphone war.`
2. `Explain why shipping containers changed the world.`
3. `Make a short about how CRISPR edits DNA for people who know nothing about biology.`
4. `Show why a bank run can destroy a healthy bank.`
5. `Make an engaging reel about the invention of the barcode.`

Regression checks:
- different topics produce different visual worlds
- no forced vintage/Vox surface treatment
- construction follows the story rather than reflexively repeating or banning cards, timelines, or stills
- HTML storyboard resolves creative direction before Remotion
- storyboard fidelity scales with uncertainty
- assets expose origin, technical, editorial, rights, and representation status
- factual evidence remains honest
- unresolved central/noun-reveal concepts compare materially different mechanisms, then select autonomously
- shot scores coordinate composition, object action, camera information, attention, rhythm, sound, and exit
- caption/disclosure loads and sound intent are reviewed before freeze
- final VO reconforms semantic events, actual readable payoff windows, and purposeful J/L cuts
- editorial and technical QA remain separate
- no user question about transitions/easing/layout unless truly necessary

## Held-out creative evaluation

These prompts and the paired cases in [behavioral-regression-prompts.md](behavioral-regression-prompts.md) are development/regression material, not a held-out creativity benchmark.

1. Before running, reserve unfamiliar briefs and factual/rights packets outside these examples: include a physical mechanism, recurring process, evidence-led history, emotional reveal, and a story where chronology is the correct job. Keep Kodak and Concorde as regression fixtures only.
2. Compare v0.8.1 and v0.9.0 using the same target small model, tools, factual packets, delivery constraints, and run conditions across several independent runs per brief. Predeclare run count and rubric; do not tune on held-out outputs or silently discard failures.
3. Save final renders and artifact-bound review evidence. Randomize pair order and hide skill version/director explanations from independent judges. First record observed visual relationships, then compare against the brief and watch the complete accessible masters.
4. Judge story-specific ideas, relationship clarity, attention/composition, object/camera choreography, pacing/payoff, sound integration, factual honesty, and story-appropriate variation. Include valid stillness, static evidence, bold captions, direct cuts, and silence so restraint is not penalized by default.
5. Track render success, gate compliance, questions asked, and repair routing separately from creative quality. Report run-level outcomes, ties, disagreement, and failures; a compliant but equally generic film is not a creative gain.

Improved small-model directing is an untested hypothesis until this comparison is actually run. Do not report the prompts, more completed fields, or deterministic validator passes as measured video-quality improvement.
