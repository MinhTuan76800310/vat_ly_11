"""
Build script for Physics 11 Deep Understanding Book.
Assembles Markdown manuscripts and figures into distribution PDF.
"""

import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BOOK_DIR = os.path.join(ROOT, 'book')
DIST_DIR = os.path.join(ROOT, 'dist')
SCRIPTS_DIR = os.path.join(ROOT, 'scripts')

os.makedirs(DIST_DIR, exist_ok=True)

def check_and_generate_figures():
    print("--> Checking and generating figures...")
    fig_script = os.path.join(SCRIPTS_DIR, 'generate_figures.py')
    result = subprocess.run([sys.executable, fig_script], cwd=ROOT)
    if result.returncode != 0:
        print("[!] Error generating figures.")
        sys.exit(1)

def build_pdf():
    check_and_generate_figures()
    
    out_pdf = os.path.join(DIST_DIR, 'vat_ly_11_chuyen_sau_chuong_01.pdf')
    chapter_src = os.path.join(BOOK_DIR, 'chapter01.md')
    metadata_file = os.path.join(BOOK_DIR, 'metadata.yaml')

    print(f"--> Compiling {chapter_src} -> {out_pdf} via Pandoc (typst engine)...")
    
    cmd = [
        'pandoc',
        chapter_src,
        f'--metadata-file={metadata_file}',
        '--resource-path=book',
        '--pdf-engine=typst',
        '-o', out_pdf
    ]
    
    result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode == 0:
        print(f"[OK] PDF build successful: {out_pdf}")
        # Print file size
        size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
        print(f"     Output size: {size_mb:.2f} MB")
    else:
        print("[!] Pandoc compilation failed.")
        sys.exit(1)

if __name__ == '__main__':
    build_pdf()
