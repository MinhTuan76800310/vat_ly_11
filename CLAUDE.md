# CLAUDE.md — Physics 11 Deep Understanding (Vật Lí 11 Chuyên Sâu)

## Goal

Build and maintain a high-quality, mathematically rigorous, and mechanism-driven physics textbook for 11th grade (`vatly_11`), based on the 2018 Vietnamese National General Education Curriculum (GDPT 2018).

---

## Autonomous Execution (ZoloMod / YOLO Mode)

- Autonomous execution is enabled: proactively inspect files, generate figures, update manuscripts, and compile the book PDF.
- Do not stop for repetitive manual confirmations when executing standard verification scripts.
- Ensure all figures and the PDF compile cleanly before concluding a task.

---

## Core Guidelines

1. **Before Authoring / Editing**:
   - Read [AGENTS.md](AGENTS.md) and [Curriculum_Syllabus.md](Curriculum_Syllabus.md).
   - Follow the 5-layer pedagogical structure (Hiện tượng/Trực giác → Mô hình hóa → Giải tích toán học → Cơ chế vi mô & Năng lượng → Phản biện & Ứng dụng).
   - Adhere to the cognitive protocol in [.agents/rules/thinking_harness.md](.agents/rules/thinking_harness.md) and prose rules in [.agents/rules/pedagogy_harness.md](.agents/rules/pedagogy_harness.md).

2. **Language Rules**:
   - **Manuscripts (`book/`)**: Vietnamese prose. English technical terms in parentheses upon first introduction.
   - **Code & Scripts**: English.
   - **Git Commits**: English, conventional commits (`feat:`, `fix:`, `docs:`, `chore:`).

3. **LaTeX / Math**:
   - Inline math: `$formula$` (ensure proper escaping).
   - Display math: `$$formula$$` on separate lines.
   - Every physical variable must be defined with its SI unit upon introduction.

---

## Build Commands

```bash
# Generate vector PDF and PNG figures
python scripts/generate_figures.py

# Compile manuscript to PDF via Pandoc and Typst
python scripts/build_book.py

# Or via Makefile
make figures
make book
make all
make clean
```
