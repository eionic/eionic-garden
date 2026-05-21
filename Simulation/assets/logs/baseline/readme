# Simulation Logs: Baseline Model

These logs represent the Standard Operating Mode (Control Group),
where Sensitivity naturally remains below 1.0,
reflecting the engine's tendency toward metabolic
preservation and homeostatic stability under these conditions.

Two log files are included, covering a combined 350-tick run
across two recording sessions:

- log_50: Ticks 6–66, 85-121, 139-201
- log_51: Ticks 6–51, 63-107, 131-202, 226-294, 325-350 (ticks redacted per data
  handling protocol)

Each file contains hormone values snapshots, fatigue,
sensitivity, rest drive, and action selection for all three
avatars (BlueY, OrangeZ, GreenX) running under identical
external conditions.

Note: INIT blocks (512-dim trait vectors) have been redacted
from all log files per Eionic Research Initiative data handling
protocol. The first 5 ticks of each file are also redacted.
Hormone trajectories and action logs are preserved as recorded.

---

### Log Structure (per tick entry)

Each tick records the following per avatar:
- Hormones: cortisol, dopamine, serotonin, oxytocin, adrenaline,
  testosterone, endorphins, melatonin
- Fatigue, Sensitivity
- Rest drive
- Action selected and associated cost

---

### Key Characteristics: Baseline Model

1. Sensitivity naturally stayed below 1.0 throughout this run
   (observed max: 0.85), without any hard ceiling imposed.
   This reflects the agent's homeostatic dynamics under the
   parameter conditions of this earlier observation period.

2. Cortisol Stabilization: High cortisol at initialization
   decays into a tight oscillation range by approximately
   Tick 75, consistent with attractor state formation from
   identical starting conditions.

3. Predictable Recovery: Correlation between Rest_drive and
   Fatigue follows a near-linear recovery pattern. The agent
   prioritizes metabolic equilibrium over high-intensity
   environmental exploration.

4. Personality Divergence: Despite identical external
   conditions, BlueY, OrangeZ, and GreenX maintain measurably
   distinct hormonal baselines. Divergence is visible in the
   raw logs from approximately Tick 75 onward.

---

### Relation to Published Paper

These logs are the source data for the comparative reference
plots (graphic_50 and graphic_51) published in the Eionic
GitHub repository. They serve as the control condition
demonstrating P4 VEE stability under conservative parameters.

The empirical tables in *Bounded Stochastic Agency*
(Eionic Research Initiative, 2026) are derived from the
Enhanced Sensitivity dataset (11,557 ticks), not this baseline.
This dataset represents an earlier, shorter observation run
used to establish initial feasibility before the full
extended run.
