import re

base_dir = r"c:\Users\Lenovo\Desktop\Projet\innov concierege\site"
html_path = rf"{base_dir}\index.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract CSS
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if css_match:
    with open(rf"{base_dir}\style.css", 'w', encoding='utf-8') as f:
        f.write(css_match.group(1).strip())

# 2. Extract JS
js_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if js_match:
    with open(rf"{base_dir}\main.js", 'w', encoding='utf-8') as f:
        f.write(js_match.group(1).strip())

# 3. Update index.html
new_content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="style.css">', content, flags=re.DOTALL)
new_content = re.sub(r'<script>.*?</script>', '<script src="main.js"></script>', new_content, flags=re.DOTALL)

# Update links
link_map = {
    '"#services"': '"services.html"',
    '"#membership"': '"abonnements.html"',
    '"#about"': '"a-propos.html"',
    '"#contact"': '"contact.html"',
    '"#home"': '"index.html"'
}
for old, new in link_map.items():
    new_content = new_content.replace(old, new)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Extract parts for other pages
head_match = re.search(r'(<!DOCTYPE html>.*?<head>.*?</head>\s*<body>)', new_content, re.DOTALL)
head_part = head_match.group(1) if head_match else ""

nav_match = re.search(r'(<!-- Navbar -->.*?</nav>)', new_content, re.DOTALL)
nav_part = nav_match.group(1) if nav_match else ""

footer_match = re.search(r'(<!-- Footer -->.*?</footer>)', new_content, re.DOTALL)
footer_part = footer_match.group(1) if footer_match else ""

scripts_part = '<script src="main.js"></script>\n</body>\n</html>'

def create_page(filename, title, hero_title, hero_desc, section_regex):
    section_match = re.search(section_regex, new_content, re.DOTALL)
    section_part = section_match.group(1) if section_match else ""
    
    page_head = head_part.replace("<title>Innov Conciergerie | L'Excellence à N'Djaména</title>", f"<title>{title} | Innov Conciergerie</title>")
    
    mini_hero = f"""
    <!-- Mini Hero -->
    <header class="hero" style="min-height: 40vh; padding-top: 6rem;">
        <div class="hero-pattern"></div>
        <div class="container">
            <h1>{hero_title}</h1>
            <p class="text-lead" style="margin-bottom: 0;">{hero_desc}</p>
        </div>
    </header>
    """
    
    page_content = page_head + "\n\n" + nav_part + "\n\n" + mini_hero + "\n\n" + section_part + "\n\n" + footer_part + "\n\n" + scripts_part
    
    with open(rf"{base_dir}\{filename}", 'w', encoding='utf-8') as f:
        f.write(page_content)

create_page("services.html", "Nos Services", "Nos Services", "Un accompagnement sur-mesure pour chaque aspect de votre vie.", r'(<!-- Services -->.*?</section>)')
create_page("abonnements.html", "Abonnements", "Nos Abonnements", "Un privilège réservé à nos membres.", r'(<!-- Membership -->.*?</section>)')
create_page("a-propos.html", "À Propos", "Notre Histoire", "Redéfinir les standards de l'excellence en Afrique Centrale.", r'(<!-- About -->.*?</section>)')
create_page("contact.html", "Contact", "Contact & Adhésion", "Votre accès au cercle Innov Conciergerie.", r'(<!-- Contact -->.*?</section>)')
