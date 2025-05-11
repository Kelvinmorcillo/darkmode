from flask import Flask, redirect, request
import datetime, locale,os, locale
# import locale 
try:

    #compability with windows
    if os.sname == "nt":
        locale_string = 'Portuguese_Portugal.1252'
    else:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except:
    pass

app = Flask(__name__)

# Helper
def get_page(filename):
    """Reads content from a file in the template folder."""
    try:
        # Use path relative to where Gunicorn likely starts (repo root)
        filepath = os.path.join("templates", filename)
        print(f"Attempting to open: {filepath}") # Add print for debugging path
        #gringo oedeia acento
        with open(filepath, "r", encoding="utf-8") as f: # Add encoding="utf-8"
            page_content = f.read()
        return page_content
   #error handling
    except FileNotFoundError:
        # Use os.getcwd() to see the actual working directory in logs
        cwd = os.getcwd(    )
        print(f"ERROR: Template file not found at RELATIVE path: {filepath}")
        print(f"Current Working Directory (CWD) was: {cwd}")
        return None
    except Exception as e:
        cwd = os.getcwd()
        print(f"ERROR: Could not read file {filepath}. CWD: {cwd}. Error: {e}")
        return None
# Home page Grey
@app.route('/', methods = ['GET'])
def index():
    # Call the helper
    page = get_page("index.html") # Pass just the filename
    if page is None:
        return "Error: index.html template indice not found!", 404
    chosen_theme_for_home = request.args.get('theme', 'default') # 'default' for gray
    page = page.replace("{theme_class}", f"{chosen_theme_for_home}-theme")
    # Do replacements
    page = page.replace("{title}", "Pagina triste de feia")
    page = page.replace("{text}", "Essa é a pagina padrão espalhafatoa")
    now = datetime.datetime.now()
    page = page.replace("{date}", now.strftime("%S-%H-%M %d:%B:%Y Até a data é feia"))
    return page
# templating
#dark
@app.route('/d', methods = ['GET'])
def dark_page():            
    page = get_page("index.html") # Pass just the filename
    if page is None:
        return "Error: index.html template indice not found!", 404
       # >>> YOU ARE MISSING THE THEME LOGIC HERE <<<
    # We need:
   # This line gets ALL arguments as a dictionary-like object, not just the 'theme' string.
    # chosen_theme = request.args
    # You need:
    chosen_theme_name = request.args.get('theme', 'dark') # Default to 'dark' for this page
    # Then use chosen_theme_name:
    page = page.replace("{theme_class}", f"{chosen_theme_name}-theme")
    now = datetime.datetime.now()
    page = page.replace("{title}", 'Dark Side')
    # Format using  locale (Portuguese)
    page = page.replace("{date}", now.strftime("%d-%B-%Y %H:%M:%S"))
    page = page.replace("{text}", 'This is the Dark Side')
    return page

#redirect d-dark
@app.route('/dark')
def redirect_dark():   
    return redirect('/d')

#white
@app.route('/w', methods = ['GET'])
def white_page():
    page = get_page("index.html") 
    if page is None:
        return "Error: index.html template indice not found!", 404
    # Do replacements
    chosen_theme_name = request.args.get('theme', 'light') # Default to 'light' for this page
    page = page.replace("{theme_class}", f"{chosen_theme_name}-theme")
    now = datetime.datetime.now()
    page = page.replace("{title}", 'White Side')
    # Format using default locale (English)
    page = page.replace("{date}", now.strftime("%d %B, %Y at %H:%M"))
    page = page.replace("{text}", 'Caminho da luz')
    return page
#redirect w-white
@app.route('/white')
def redirect_white():
    return redirect('/w')


# --- Standard Run Settings ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable
    app.run(host="0.0.0.0", port=port)  # Listen on 0.0.0.0 and use the specified port

