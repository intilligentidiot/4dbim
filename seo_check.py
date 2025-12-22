import os
import re
from html.parser import HTMLParser

class SEOParser(HTMLParser):
    def __init__(self, current_file, root_dir):
        super().__init__()
        self.current_file = current_file
        self.root_dir = root_dir
        self.links = []
        self.images = []
        self.meta_tags = {}
        self.link_tags = []
        self.headings = []
        self.has_responsive_classes = False
        self.title_tag = False
        self.doc_structure = [] # To track tag order if needed

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        if tag == 'a':
            if 'href' in attrs_dict:
                self.links.append({
                    'href': attrs_dict['href'],
                    'title': attrs_dict.get('title')
                })
        
        if tag == 'img':
            src = attrs_dict.get('src', '')
            width = attrs_dict.get('width')
            height = attrs_dict.get('height')
            alt = attrs_dict.get('alt')
            loading = attrs_dict.get('loading')
            self.images.append({
                'src': src,
                'width': width,
                'height': height,
                'alt': alt,
                'loading': loading
            })

        if tag == 'meta':
            name = attrs_dict.get('name')
            property = attrs_dict.get('property')
            content = attrs_dict.get('content')
            if name:
                self.meta_tags[name] = content
            if property:
                self.meta_tags[property] = content

        if tag == 'link':
            rel = attrs_dict.get('rel')
            href = attrs_dict.get('href')
            self.link_tags.append({'rel': rel, 'href': href})

        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.headings.append(tag)

        if tag == 'title':
            self.title_tag = True

        # Heuristic for responsiveness check
        for key, value in attrs_dict.items():
            if value and any(bp in value for bp in ['sm:', 'md:', 'lg:', 'xl:', '2xl:']):
                self.has_responsive_classes = True

def check_file_existence(link, current_file, root_dir):
    if not link: return False
    if link.startswith('http') or link.startswith('#') or link.startswith('mailto:'):
        return True # External or anchor or mailto, skip
    
    # Handle absolute path from root if starts with /
    if link.startswith('/'):
        target_path = os.path.join(root_dir, link.lstrip('/'))
    else:
        # Relative path
        base_dir = os.path.dirname(current_file)
        target_path = os.path.join(base_dir, link)
    
    # Remove anchor part
    if '#' in target_path:
        target_path = target_path.split('#')[0]
        
    return os.path.exists(target_path) or os.path.exists(target_path.replace('%20', ' '))

def main():
    root_dir = r"c:\4D\4dbim"
    html_files = []
    
    # Find all HTML files
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    all_linked_files = set()
    errors = []
    warnings = []
    
    print("--- 24-Point Technical SEO & Site Health Audit ---\n")

    for file_path in html_files:
        rel_path = os.path.relpath(file_path, root_dir)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        parser = SEOParser(file_path, root_dir)
        parser.feed(content)
        
        # 1. Image Optimization (WebP, Dimensions, Alt, Lazy)
        for img in parser.images:
            src = img['src']
            if not src or src.strip() == "" or src == "#": 
                 warnings.append(f"[Empty Image Src] In {rel_path}: Image has empty or '#' src.")
                 continue

            if not src.lower().endswith('.webp') and not src.startswith('http'):
                errors.append(f"[Legacy Image Format] In {rel_path}: Image {src} is not WebP.")
            
            if not img['width'] or not img['height']:
                 warnings.append(f"[Missing Dimensions] In {rel_path}: Image {src} missing width/height.")
            
            if not img['alt']:
                 warnings.append(f"[Missing Alt Text] In {rel_path}: Image {src} missing alt text.")
            
            if img['loading'] != 'lazy' and 'banner' not in src.lower(): # Heuristic: Assume banner might be LCP
                 warnings.append(f"[Missing Lazy Load] In {rel_path}: Image {src} missing loading='lazy'.")

            # Check existence
            if not check_file_existence(src, file_path, root_dir):
                errors.append(f"[Broken Image] In {rel_path}: {src} not found.")

        # 2. Meta Tags (Title, Desc, Keywords, Robots, Theme Color)
        if not parser.title_tag:
            errors.append(f"[Missing Title] In {rel_path}: No <title> tag found.")
        if 'description' not in parser.meta_tags:
            errors.append(f"[Missing Meta Description] In {rel_path}")
        if 'keywords' not in parser.meta_tags:
            warnings.append(f"[Missing Meta Keywords] In {rel_path}")
        if 'robots' not in parser.meta_tags:
            warnings.append(f"[Missing Meta Robots] In {rel_path}")
        if 'theme-color' not in parser.meta_tags:
            warnings.append(f"[Missing Theme Color] In {rel_path}")

        # 3. Canonical Link
        has_canonical = any(l.get('rel') == 'canonical' for l in parser.link_tags)
        if not has_canonical:
            warnings.append(f"[Missing Canonical] In {rel_path}")

        # 4. Content Structure (H1)
        if 'h1' not in parser.headings:
            errors.append(f"[Missing H1] In {rel_path}: No <h1> tag found.")
        if parser.headings.count('h1') > 1:
            warnings.append(f"[Multiple H1] In {rel_path}: Found {parser.headings.count('h1')} <h1> tags.")

        # 5. Broken Links & Anchor Titles
        for link in parser.links:
            href = link['href']
            if not check_file_existence(href, file_path, root_dir):
                errors.append(f"[Broken Link] In {rel_path}: {href} not found")
            else:
                # Track for orphan check
                if href and not (href.startswith('http') or href.startswith('#') or href.startswith('mailto:')):
                    if href.startswith('/'):
                        target = os.path.join(root_dir, href.lstrip('/'))
                    else:
                        target = os.path.join(os.path.dirname(file_path), href)
                    if '#' in target: target = target.split('#')[0]
                    all_linked_files.add(os.path.abspath(target))
            
            # if not link['title']:
            #     warnings.append(f"[Missing Anchor Title] In {rel_path}: Link to {href} missing title attribute.")

        # 6. Social Tags (OG, Twitter)
        if 'og:title' not in parser.meta_tags or 'og:image' not in parser.meta_tags:
             warnings.append(f"[Missing OpenGraph] In {rel_path}: Missing og:title or og:image.")
        if 'twitter:card' not in parser.meta_tags:
             warnings.append(f"[Missing Twitter Card] In {rel_path}: Missing twitter:card.")

    # Orphan Check
    orphans = []
    # Add index.html and 404.html as valid entry points
    all_linked_files.add(os.path.join(root_dir, 'index.html'))
    all_linked_files.add(os.path.join(root_dir, '404.html'))
    
    for file_path in html_files:
        if os.path.abspath(file_path) not in all_linked_files:
            orphans.append(os.path.relpath(file_path, root_dir))

    print("\n[Critical Errors]")
    if errors:
        for err in errors: print(err)
    else:
        print("None (Good Job!)")

    print("\n[Warnings]")
    if warnings:
        for warn in warnings: print(warn)
    else:
        print("None")

    print("\n[Orphan Pages]")
    if orphans:
        for orphan in orphans: print(orphan)
    else:
        print("None")

if __name__ == "__main__":
    main()
