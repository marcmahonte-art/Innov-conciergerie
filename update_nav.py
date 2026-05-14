import glob
import os

base_dir = r"c:\Users\Lenovo\Desktop\Projet\innov concierege\site"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

target_str = '<ul class="nav-links" id="nav-links">\n                <li><a href="services.html"'
replacement_str = '<ul class="nav-links" id="nav-links">\n                <li><a href="index.html" class="nav-link">Accueil</a></li>\n                <li><a href="services.html"'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_str in content:
        new_content = content.replace(target_str, replacement_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Target not found in {file}")
