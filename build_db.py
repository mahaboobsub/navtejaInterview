import json
import os

DB_PATH = 'modules.json'
HTML_TEMPLATE_PATH = 'index.html'

def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_db(db):
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def compile_html():
    db = load_db()
    if not db:
        print("Database is empty. Cannot compile.")
        return
    
    # Read index_template.html
    template_path = 'index_template.html'
    if not os.path.exists(template_path):
        # Backup index.html to index_template.html if it contains the placeholder
        if os.path.exists('index.html'):
            with open('index.html', 'r', encoding='utf-8') as f:
                content = f.read()
            if 'MODULES_DATA_SCRIPT' in content:
                with open(template_path, 'w', encoding='utf-8') as f:
                    f.write(content)
            else:
                print("Error: index.html already compiled and no template exists.")
                return
        else:
            print("Error: index.html not found.")
            return

    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Generate the script content
    js_data = json.dumps(db, ensure_ascii=False)
    
    # We replace the placeholder with the serialized JSON data
    compiled_html = html.replace("MODULES_DATA_PLACEHOLDER", js_data)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(compiled_html)
    print("Successfully compiled index.html with database.")

if __name__ == '__main__':
    compile_html()
