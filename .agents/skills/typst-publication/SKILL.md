---
name: typst-publication
description: >-
  Publication-grade document design and PDF compilation using Typst.
  Use whenever the user requests a 'bản pdf đẹp', scientific handout,
  standalone study guide, or publication-ready document.
---

# Typst Publication Design & PDF Compilation Skill

## 1. When to Use
Activate this skill whenever the user requests:
- "bản pdf đẹp", "sách đẹp", "handout đẹp", "tài liệu đẹp".
- Standalone study modules, cheat sheets, or article summaries requiring professional graphic design.

## 2. Layout & Typography Invariants
1. **Font Pairing**:
   - Body: `Libertinus Serif`, `Cambria`, or `Palatino Linotype` (size 9.8pt - 10.5pt, leading 0.62em - 0.65em).
   - Math: `New Computer Modern Math` or `Cambria Math`.
   - Headings: Bold sans-serif or clean serif with distinct level colors (Deep Navy `#0f172a`, Slate `#1e3a8a`).
2. **Modern Header Banner**:
   - Title card with dark slate background (`#0f172a`), metadata tags (Level, Topic, Date), and subtitle.
3. **Unbreakable Card Blocks (`breakable: false`)**:
   - All callout boxes, state cards, and summary tables MUST have `breakable: false` to avoid ugly mid-card page splits.
4. **Vector PDF Figures**:
   - Always embed vector `.pdf` figures (`image("figures/fig.pdf", width: ...)`), NEVER low-res raster images when PDFs are available.
5. **Context Headers & Footers (Typst 0.15+)**:
   ```typst
   header: context {
     if counter(page).get().first() > 1 [ ... ]
   },
   footer: context [
     #line(length: 100%, stroke: 0.5pt + rgb("cbd5e1"))
     #grid(columns: (1fr, 1fr), align: (left, right),
       [ Document Subtitle ],
       [ Page #counter(page).display() of #counter(page).final().first() ]
     )
   ]
   ```

## 3. Typst Syntax Pitfalls to Avoid
- ❌ Do NOT write `* *Bold Title:*` for bullet lists. Typst's parser confuses multiple asterisks with unclosed bold delimiters.
  ✅ Use `- *Bold Title:*` instead.
- ❌ Do NOT use `vec(u)_1` for vector arrows (it creates a column matrix).
  ✅ Use `arrow(u)_1` or `bold(u)_1`.
- ❌ Do NOT use `**bold**` (Markdown style).
  ✅ Use `*bold*` (Typst style).

## 4. Strict Page Budgeting & Verification Loop
Never deliver a PDF with orphan pages (pages with only 1-2 lines). Always follow this verification pipeline:
1. `typst compile input.typ output.pdf`
2. `typst compile --format png --ppi 150 input.typ 'preview/page_{p}.png'`
3. Inspect the last generated page with `view_file`.
4. If the last page has under 5 lines, adjust margins (e.g. from 2.2cm to 2.0cm) or image sizes (from 88% to 75%) until the document fits into an exact, balanced page budget.
