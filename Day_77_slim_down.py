from flask import Flask, redirect
import datetime
# from datetime import date # Not needed if using datetime.datetime/datetime.date
import os
# import locale # Keep commented out

app = Flask(__name__)

# --- Path setup (COMMENTED OUT - Using relative paths directly below) ---
# script_dir = os.path.dirname(os.path.abspath(__file__))
# template_folder = os.path.join(script_dir, "template")

@app.route('/')
def index():
    # Call the helper
    page = get_page("index.html") # Pass just the filename
    if page is None:
        return "Error: index.html template not found!", 404
    # Do replacements
    page = page.replace("{title}", "Beatles")
    page = page.replace("{text}", "Esse é o indice")
    page = page.replace("{date}", str(datetime.date.today()))
    return page

def get_page(filename):
    """Reads content from a file in the template folder."""
    # --- Construct relative path assuming 'template' is in the root ---
    try:
        # Use path relative to where Gunicorn likely starts (repo root)
        filepath = os.path.join("template", filename)
        print(f"Attempting to open: {filepath}") # Add print for debugging path
        with open(filepath, "r") as f:
            page_content = f.read()
        return page_content
    except FileNotFoundError:
        # Use os.getcwd() to see the actual working directory in logs
        cwd = os.getcwd()
        print(f"ERROR: Template file not found at RELATIVE path: {filepath}")
        print(f"Current Working Directory (CWD) was: {cwd}")
        return None
    except Exception as e:
        cwd = os.getcwd()
        print(f"ERROR: Could not read file {filepath}. CWD: {cwd}. Error: {e}")
        return None

# ... (Keep the rest of your routes: /and-i-say-hello, /you-say-bye) ...
# Make sure hello_page and bye_page also call get_page("index.html")

@app.route('/and-i-say-hello')
def hello_page():
    page = get_page('index.html') # Call with filename
    if page is None:
        return "Error: Template file not found!", 404
    now = datetime.datetime.now()
    page = page.replace("{title}", 'Hello Page')
    # Format using default locale (English)
    page = page.replace("{date}", now.strftime("%Y-%m-%d %H:%M:%S"))
    page = page.replace("{text}", 'And I say HELLO!')
    return page

@app.route('/you-say-bye')
def bye_page():
    page = get_page('index.html') # Call with filename
    if page is None:
        return "Error: Template file not found!", 404
    now = datetime.datetime.now()
    page = page.replace("{title}", 'Goodbye Page')
    # Format using default locale (English)
    page = page.replace("{date}", now.strftime("%B %d, %Y at %H:%M"))
    page = page.replace("{text}", 'You say GOODBYE!')
    return page

# ... (Keep the redirect routes: /hello, /bye) ...
@app.route('/hello')
def redirect_hello():
    return redirect('/and-i-say-hello')
@app.route('/bye')
def redirect_bye():
    return redirect('/you-say-bye')

# --- Standard Run Settings ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host="0.0.0.0", port=port)  # Listen on 0.0.0.0 and use the specified port










"""from flask import Flask, redirect
import datetime
from datetime import date # Keep this if you use it for the date replacement
import os # <--- Make sure os is imported
# import locale # <-- Comment out

# --- Try setting the locale for Portuguese time formatting ---
# locale_string = 'Portuguese_Portugal.1252' # <-- Comment out

# try: # <-- Comment out
#     locale.setlocale(locale.LC_TIME, locale_string) # <-- Comment out
#     print(f"Successfully set locale to {locale_string}") # <-- Comment out
# except locale.Error as e: # <-- Comment out
#     print(f"Warning: Could not set locale to {locale_string}. Date formatting might remain in English. Error: {e}") # <-- Comment out

app = Flask(__name__)
# ... rest of your code ...
#flasksucks

# --- Calculate absolute path to template folder ---
script_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(script_dir, "template") # Assumes folder is named 'template'

app = Flask(__name__)



@app.route('/')
def index():
    page = get_page("index.html")  # Call the helper
    if page is None:
        return "Error: index.html template not found!", 404
    page = page.replace("{title}", "Beatles")
    page = page.replace("{text}", "Esse é o indice")
    page = page.replace("{date}", str(datetime.date.today()))  # Example date
    return page

def get_page(filename):
    Reads content from a file in the template folder.
    filepath = os.path.join(template_folder, filename)
    try:
        with open(filepath, "r") as f:
            page_content = f.read()
        return page_content
    except FileNotFoundError:
        print(f"ERROR: Template file not found at {filepath}")
        return None
    except Exception as e:
        print(f"ERROR: Could not read file {filepath}: {e}")
        return None

@app.route('/and-i-say-hello')
def hello_page():
    page = get_page('index.html')
    page = page.replace("{title}", 'hello')
    page = page.replace("{date}", datetime.datetime.now().strftime("%H:%M:%S Dia %d de %B de %Y"))
    page = page.replace("{text}", 'hello')
    return page

@app.route('/you-say-bye')
def bye_page():
    page = get_page('index.html')
    page = page.replace("{title}", 'bye')
    page = page.replace("{date}", datetime.datetime.now().strftime("%H:%M:%S Dia %d de %B de %Y"))
    page = page.replace("{text}", 'bye')
    return page

@app.route('/hello')
def redirect_hello():
    return redirect('/and-i-say-hello')

@app.route('/bye')
def redirect_bye():
    return redirect('/you-say-bye')

# --- Standard Run Settings ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host="0.0.0.0", port=port)  # Listen on 0.0.0.0 and use the specified port

# --- Standard Run Settings ---
#if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
#    app.run(host="0.0.0.0", port=port)  # Listen on 0.0.0.0 and use the specified port
##ttesssstt"""