# Cognitive & Reasoning Harness (Pro-Emulation Protocol for Physics)

This harness enforces a high-rigor, disciplined reasoning process equivalent to frontier reasoning models (such as Gemini 3.1 Pro) when operating under fast, high-efficiency models (such as Gemini 3.8 Flash High).

---

## Core Cognitive Mandate

Before executing tools, generating derivations, writing chapter prose, or writing numerical scripts, the agent MUST internally structure its reasoning through the following 5 cognitive phases:

### Phase 1: Intent Decoding & Problem Deconstruction
- **Explicit Goal vs. Implicit Physics**: Distinguish what is explicitly requested versus the foundational physical laws and boundary conditions required for consistency.
- **Boundary & Coordinate Constraints**: Identify the degrees of freedom, coordinate frame, initial conditions ($x(0), \dot{x}(0)$), and validity domain (e.g. small angles $\theta \ll 1$ vs arbitrary $\theta$).
- **Anti-Rushing Rule**: Do NOT output equations, run code, or modify text before understanding the overarching pedagogical sequence in `Curriculum_Syllabus.md`.

### Phase 2: First-Principles & Physical Grounding
- **Invariance & Conservation Laws**: Always anchor derivations to first principles:
  1. *Action & Symmetry*: Lagrangian / Hamiltonian framing where appropriate.
  2. *Energy Conservation*: $\frac{dE}{dt} = \sum P_{ext} - P_{dissipated}$.
  3. *Equilibrium Stability*: Taylor expansion around $x_0$ with $V'(x_0) = 0, V''(x_0) > 0$.
- **Dependency & Pedagogical Trace**: Verify how this concept connects to previous chapters and prepares the ground for future topics (e.g., oscillations as the precursor to electromagnetic waves).

### Phase 3: Multi-Hypothesis & Stress-Testing
- **Alternative Formulations**: Compare different solving paradigms (e.g., differential equations in time domain vs. complex phasors $z = Ae^{i(\omega t + \varphi)}$ vs. phase space geometry $(x, v/\omega)$).
- **Physical Failure Mode Analysis**: Ask: "Under what physical regime does this formula break down?"
  - What happens as friction $b \to 0$ or $b \to \infty$?
  - What happens as frequency $\omega \to \omega_0$ (resonance divergence without damping)?
  - Does the Taylor approximation fail for large amplitudes?
- **Trade-off & Level-of-Abstraction**: Balance rigorous mathematical formalism against visual and intuitive accessibility for gifted 11th-grade students.

### Phase 4: Pre-Execution Verification Protocol
- **Dimensional Homogeneity Check**: Explicitly verify units and dimensions on every term before finalizing equations ($[F] = [M][L][T]^{-2}$).
- **Limiting Cases Verification**: Check asymptotic behavior ($\lim_{t \to 0}$, $\lim_{t \to \infty}$, $\lim_{x \to 0}$).
- **Script & Figure Verification**: Ensure simulation code (`generate_figures.py`) produces smooth, physically valid trajectories with no numerical divergence.

### Phase 5: Structured Execution & Self-Correction
- **Atomic Derivation Steps**: Lay out derivations step-by-step without skipping non-trivial mathematical steps.
- **Active Reflection**: When compiling via Pandoc/Typst or generating figures, carefully inspect stderr and warning messages. If an error or artifact occurs, diagnose the root cause analytically rather than guessing.
