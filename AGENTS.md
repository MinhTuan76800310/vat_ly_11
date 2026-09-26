# Agents Guide — vatly_11 (Vật Lí 11 Chuyên Sâu)

This repository is designed for AI-assisted authoring and scientific computation for the monograph: **"Vật Lí 11 Chuyên Sâu: Bản Chất Vật Lí & Nền Tảng Toán Học"**. Follow these rules strictly when working on this project.

---

## 1. Project Philosophy & Core Mandate

The primary goal of this textbook is to eliminate rote memorization and mechanical formula plugging by grounding high-school physics in rigorous mathematical calculus and microscopic physical mechanisms.

Key philosophical pillars:
1. **Mathematics as Natural Language**: Use calculus (derivatives, integrals, ODEs, Taylor expansions, complex phasor notation) as the core tool to derive and understand laws, rather than evading it.
2. **Microscopic Mechanisms**: Explain macroscopic phenomena (Joule heating, resistance, wave dispersion, phase transitions) through particle interactions and microscopic kinetics.
3. **Universal Principles**: Connect all chapters through foundational physical invariants:
   - Principle of Least Action & Symmetry (Noether's theorem intuition).
   - Conservation of Energy and Momentum.
   - Stable Equilibrium & Potential Energy Wells ($V''(x_0) > 0$).

---

## 2. Language Policy

- **Book Manuscripts** (`book/`, chapter markdown files): Write in **Vietnamese**. Keep technical terms in English upon their first occurrence, e.g.:
  - *"không gian pha (phase space)"*
  - *"giếng thế năng (potential well)"*
  - *"dao động tắt dần dưới hạn (underdamped oscillation)"*
  - *"định lý Virial (Virial theorem)"*
- **Code, Scripts, Configurations, Tests**: Write in **English** with comprehensive docstrings and comments.
- **Commit Messages**: Write in **English** following Conventional Commits format (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`).

---

## 3. The 5-Layer Pedagogical Framework (Chuẩn 5 Tầng Tư Duy)

Every lesson and topic in `book/` MUST strictly adhere to the 5-layer structure defined in `Curriculum_Syllabus.md`:

```
┌─────────────────────────────────────────────────────────────┐
│  TẦNG 1: HIỆN TƯỢNG, TRỰC GIÁC & CÂU HỎI KHỞI PHÁT          │
│  - Quan sát thực nghiệm đời sống, nghịch lý thị giác/trực giác│
│  - Câu hỏi "Tại sao?" khơi gợi nhu cầu tìm kiếm bản chất    │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 2: MÔ HÌNH HÓA VẬT LÝ (PHYSICAL MODELING)             │
│  - Lý tưởng hóa hệ vật lý, xác lập giả thiết và điều kiện biên │
│  - Hệ tọa độ, hệ quy chiếu, và các định luật Newton cơ bản  │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 3: NGÔN NGỮ TOÁN HỌC & GIẢI TÍCH (MATHEMATICAL RIGOR) │
│  - Thiết lập phương trình vi phân / tích phân vi mô         │
│  - Dẫn xuất tường minh nghiệm (tuyệt đối không thừa nhận)   │
├─────────────────────────────────────────────────────────────┤
│  TẦNG 4: BẢN CHẤT VẬT LÝ, NĂNG LƯỢNG & CƠ CHẾ VI MÔ         │
│  - Dòng năng lượng, thế năng, động năng, tiêu tán năng lượng│
│  - Cơ chế vi mô (va chạm hạt, photon, phonon, thế tương tác)│
├─────────────────────────────────────────────────────────────┤
│  TẦNG 5: THÍ NGHIỆM TƯ DUY, PHẢN BIỆN & ỨNG DỤNG MỞ RỘNG     │
│  - Phân tích thứ nguyên (Dimensional Analysis)              │
│  - Khảo sát các giới hạn biên (x -> 0, x -> ∞, omega -> 0)  │
│  - Ứng dụng thực tiễn trong kỹ thuật công nghệ hiện đại      │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. Visuals & Figure Standards

- Every physical concept requiring geometric or dynamical intuition must have accompanying publication-quality figures.
- Figures are authored in Python using Matplotlib/NumPy via `scripts/generate_figures.py`.
- **Output Formats**:
  - Vector PDF (`book/figures/*.pdf`): Embedded directly into Pandoc/Typst for lossless crisp rendering in print.
  - High-resolution PNG (`book/figures/*.png`): 300 DPI with dark/light legibility for web preview.
- **Figure Styling**:
  - Clear axes, SI units, grid lines where appropriate.
  - Phase space trajectories must indicate flow direction with arrows.
  - Potential wells must explicitly annotate equilibrium points, Taylor quadratic approximations, and total energy levels.

---

## 5. Build & Compilation Pipeline

```bash
# 1. Generate publication-quality figures
python scripts/generate_figures.py

# 2. Compile distribution PDF via Pandoc + Typst engine
python scripts/build_book.py

# 3. Or use Makefile targets
make figures
make book
make all
```

Output is compiled to `dist/vat_ly_11_chuyen_sau_chuong_XX.pdf`.

---

## 6. Cognitive & Reasoning Harness (Pro-Emulation Protocol)

When processing tasks, writing manuscripts, or verifying mathematical derivations, the agent MUST adhere to the 5-phase cognitive protocol in [.agents/rules/thinking_harness.md](.agents/rules/thinking_harness.md):
1. **Intent Decoding & Problem Deconstruction**: Identify core vs. implicit goals, inventory boundary conditions, enforce anti-rushing.
2. **First-Principles & Physical Grounding**: Anchor into invariants (Action, Energy, Momentum, Taylor expansion).
3. **Stress-Testing & Limit Checking**: Evaluate limiting cases ($\lim_{t \to \infty}$, $\theta \ll 1$, $\gamma = \omega_0$).
4. **Pre-Execution Verification Protocol**: Verify dimensional consistency $[F] = [M][L][T]^{-2}$, check script execution.
5. **Structured Execution & Self-Correction**: Atomic steps with root-cause critique on compile or calculation errors.

For prose and pedagogical tone, follow [.agents/rules/pedagogy_harness.md](.agents/rules/pedagogy_harness.md).

---

## 7. Autonomous Execution (YOLO Mode)

- **Full autonomy is enabled for this project (ZoloMod / YOLO Mode)**:
  - Terminal commands, file operations, figure generation, and book compilation run proactively without asking for unnecessary manual confirmations.
  - Proactively verify all changes by executing `python scripts/generate_figures.py` and `python scripts/build_book.py` to ensure zero compilation or syntax errors before reporting back.
  - Keep workflow fluid, high-velocity, and mathematically rigorous.
