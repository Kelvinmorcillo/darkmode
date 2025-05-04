from flask import Flask, redirect
import datetime
from datetime import date # Keep this if you use it for the date replacement
import os # <--- Make sure os is imported
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
app = Flask(__name__)

# --- Calculate absolute path to template folder ---
script_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(script_dir, "template") # Assumes folder is named 'template'

@app.route('/') # <--- Assuming you want this route, not '/hello' for this code
def index():
    # Example: Read and return the index.html content for the main page
    page = get_page("index.html") # Call the helper
    if page is None:
        return "Error: index.html template not found!", 404
    # You could do replacements here too if needed
    page = page.replace("{title}", "Beatles")
    page = page.replace("{text}", "Esse é o indice")
    page = page.replace("{date}", str(datetime.date.today())) # Example date
    return page

def get_page(filename):
    """Reads content from a file in the template folder."""
    # Construct the full path inside the function
    filepath = os.path.join(template_folder, filename)
    try:
        with open(filepath, "r") as f:
            page_content = f.read()
        return page_content
    except FileNotFoundError:
        print(f"ERROR: Template file not found at {filepath}")
        return None # Return None if file not found
    except Exception as e:
        print(f"ERROR: Could not read file {filepath}: {e}")
        return None # Return None on other errors
@app.route('/and-i-say-hello')
def hello_page():
    page = get_page('index.html')
            # --- Make replacements (ensure placeholders match HTML) ---
    page = page.replace("{title}", 'hello') # Example title
    page = page.replace("{date}", datetime.datetime.now().strftime("%H:%M:%S Dia %d de %B de  %Y"))
    page = page.replace("{text}", 'hello') # Example text
    return page

@app.route('/you-say-bye')
def bye_page():
    page = get_page('index.html')
    
    # --- Make replacements (ensure placeholders match HTML) ---
    page = page.replace("{title}", 'bye') # Example tile
    page = page.replace("{date}", datetime.datetime.now().strftime("%H:%M:%S Dia %d de %B de  %Y"))
    page = page.replace("{text}", 'bye') # Example text
    return page

@app.route('/hello')
def redirect_hello():
    return redirect('/and-i-say-hello')
@app.route('/bye')
def redirect_bye():
    return redirect('/you-say-bye')
# --- Standard Run Settings ---
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
