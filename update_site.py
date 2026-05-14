import glob
import os
import re

base_dir = r"c:\Users\Lenovo\Desktop\Projet\innov concierege\site"

# 1. Update style.css
css_path = os.path.join(base_dir, "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Add background to .hero
if "background-image: url('hero-bg.png');" not in css_content:
    css_content = css_content.replace(
        "background-color: var(--color-deep-bordeaux);",
        "background-color: var(--color-deep-bordeaux);\n            background-image: url('hero-bg.png');\n            background-size: cover;\n            background-position: center;"
    )

# Adjust overlay transparency
css_content = css_content.replace(
    "linear-gradient(rgba(74, 12, 24, 0.8), rgba(74, 12, 24, 0.95))",
    "linear-gradient(rgba(74, 12, 24, 0.5), rgba(74, 12, 24, 0.8))"
)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_content)

# 2. Update HTML files to remove logo-text
html_files = glob.glob(os.path.join(base_dir, "*.html"))
logo_text_regex = re.compile(r'<div class="logo-text">\s*<span class="logo-title">INNOV</span>\s*<span class="logo-subtitle">CONCIERGERIE</span>\s*</div>', re.DOTALL)

for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    new_html, count = logo_text_regex.subn('', html_content)
    if count > 0:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Removed {count} logo-text blocks from {os.path.basename(html_file)}")
