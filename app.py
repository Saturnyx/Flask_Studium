import datetime
import os
import secrets

from flask import Flask, render_template, redirect, request, Blueprint
from flask_compress import Compress
from jinja2 import TemplateNotFound
from markupsafe import Markup

from lib import clear_logs, render, search_files

version = "12025.0.0"  # Current Version Number
port_number = 47777  # Port Number to use during testing
UPLOAD_FOLDER = "uploads"  # The folder where notes are submitted

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
xperiments = Blueprint("admin", __name__, template_folder="xperiments")
app.register_blueprint(xperiments, url_prefix="/xperiment")
Compress(app)


# MAIN PAGES ----------------------------------------------------------------------------------------------------------+
@app.route("/")
def home():
    author = "Harshal"
    return render_template("index.html", version=version, copyright=author)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_query = request.form.get("search_query", "").strip()
        if not search_query:
            return render_template(
                "search.html", content='<p class="mono">No search query provided.</p>'
            )
        raw_results = search_files(search_query)
        for i in range(len(raw_results)):
            raw_results[i] = (
                raw_results[i].replace("library\\", "").replace("library/", "")
            )
            raw_results_path = raw_results[i].replace(".html", "")
            raw_results_text = raw_results[i].replace(".html", "")
            raw_results[i] = f'<a href="/{raw_results_path}">{raw_results_text}</a>'
        final_result = Markup(
            "<p class='search_result'>" + "<br>".join(raw_results) + "</p>"
        )
        return render_template("search.html", content=final_result)
    else:
        return render_template("search.html", content="")


@app.route("/guide")
def guide():  # put application's code here
    title = "Guide"
    author = "Harshal"
    path = "guide.html"
    return render(title, author, path)


@app.route("/help")
def help_page():  # put application's code here
    title = "Help"
    author = "Harshal"
    path = "help.html"
    return render(title, author, path)


@app.route("/about_studium")
def about_studium():  # put application's code here
    title = "About Studium"
    author = "Harshal"
    path = "about_studium.html"
    return render(title, author, path)


@app.route("/about_us")
def about_us():
    title = "About Us"
    author = "Harshal"
    path = "about_us.html"
    return render(title, author, path)


@app.route("/quotes")
def a_quote_a_day():
    title = "A Quote A Day"
    author = "Harshal"
    path = "aquoteaday.html"
    return render(title, author, path)


# BIOLOGY -------------------------------------------------------------------------------------------------------------+
@app.route("/biology/biology")
def biology():
    title = "Biology"
    author = "Harshal"
    path = "biology/biology.html"
    return render(title, author, path)


# CHEMISTRY -----------------------------------------------------------------------------------------------------------+
@app.route("/chemistry/chemistry")
def chemistry():
    title = "Chemistry"
    author = "Harshal"
    path = "chemistry/chemistry.html"
    return render(title, author, path)


@app.route("/chemistry/")
def chem():
    return redirect("/chemistry/chemistry")


# INORGANIC CHEMISTRY
@app.route("/chemistry/inorganic_chemistry/inorganic_chemistry")
def inorganic_chemistry():
    title = "Inorganic Chemistry"
    author = "Harshal"
    path = "chemistry/inorganic_chemistry/inorganic_chemistry.html"
    return render(title, author, path)


@app.route("/chemistry/inorganic_chemistry/atoms")
def atoms():
    title = "Atoms"
    author = "Harshal"
    path = "chemistry/inorganic_chemistry/atoms.html"
    return render(title, author, path)


@app.route("/chemistry/inorganic_chemistry/periodic_table")
def periodic_table():
    title = "Periodic Table"
    author = "Harshal"
    path = "chemistry/inorganic_chemistry/periodic_table.html"
    return render(title, author, path)


# ORGANIC CHEMISTRY
@app.route("/chemistry/organic_chemistry/organic_chemistry")
def organic_chemistry():
    title = "Organic Chemistry"
    author = "Harshal"
    path = "chemistry/organic_chemistry/organic_chemistry.html"
    return render(title, author, path)


# COMPUTER SCIENCE ----------------------------------------------------------------------------------------------------+
@app.route("/computer_science/computer_science")
def computer_science():
    title = "Computer Science"
    author = "Harshal"
    path = "computer_science/computer_science.html"
    return render(title, author, path)


# MATHEMATICS ---------------------------------------------------------------------------------------------------------+


@app.route("/mathematics/mathematics")
def mathematics():
    title = "Mathematics"
    author = "Harshal"
    path = "mathematics/mathematics.html"
    return render(title, author, path)


# PHYSICS -------------------------------------------------------------------------------------------------------------+
@app.route("/physics/physics")
def physics():
    title = "Physics"
    author = "Harshal"
    path = "physics/physics.html"
    return render(title, author, path)


# CONTRIBUTING --------------------------------------------------------------------------------------------------------+
@app.route("/contribute")
def contribute():
    title = "Contribute"
    author = "Harshal"
    path = "contributions/contribute.html"
    return render(title, author, path)


@app.route("/contribute/notes", methods=["GET", "POST"])
def contribute_notes():
    title = "Submit Notes"
    author = "Harshal"
    path = "contributions/notes.html"
    return render(title, author, path)


@app.route("/submit", methods=["GET", "POST"])
def handle_submission():
    # Get form data
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    title = request.form.get("title", "").strip()
    files = request.files.getlist("file")

    if not name:
        return "Error: Name is required.", 400
    if not files:
        return "Error: No files uploaded.", 400

    folder_path = os.path.join(UPLOAD_FOLDER, name)

    os.makedirs(folder_path, exist_ok=True)

    info_file_path = os.path.join(folder_path, "info.txt")
    with open(info_file_path, "a") as info_file:
        info_file.write(
            f"Submission time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        info_file.write(f"Name: {name}\n")
        info_file.write(f"Email: {email}\n")
        info_file.write(f"Title: {title}\n")
        info_file.write("-" * 50 + "\n")

    for file in files:
        if file.filename:
            save_path = os.path.join(folder_path, file.filename)
            file.save(save_path)
    print(folder_path)
    if os.path.exists(folder_path):
        return redirect("/contribute/success")
    else:
        return redirect("/contribute/failure")


@app.route("/contribute/success")
def contribute_success():
    title = "Success"
    author = "Harshal"
    path = "contributions/success.html"
    return render(title, author, path)


@app.route("/contribute/failure")
def contribute_failure():
    title = "Failure"
    author = "Harshal"
    path = "contributions/failure.html"
    return render(title, author, path)


# ERRORS --------------------------------------------------------------------------------------------------------------+
@app.errorhandler(404)
def page_not_found(e):
    title = "Page Not Found"
    author = "Harshal"
    path = "errors/404.html"
    return render(title, author, path)


@app.errorhandler(400)
def bad_request(e):
    title = "Bad Request"
    author = "Harshal"
    path = "errors/400.html"
    error = (
        "@ "
        + str(datetime.datetime.now())
        + " error: 400 by "
        + request.remote_addr
        + "\n"
    )
    with open("logs/error.log", "a") as error_file:
        error_file.write(error)
    return render(title, author, path)


@app.errorhandler(500)
def server_error(e):
    error = (
        "@ "
        + str(datetime.datetime.now())
        + " error: 500 by "
        + request.remote_addr
        + "\n"
    )
    with open("logs/main.log", "a") as log_file:
        log_file.write(error)
    with open("logs/error.log", "a") as error_file:
        error_file.write(error)
    print(error)
    title = "Server Error"
    author = "Harshal"
    path = "errors/500.html"
    return render(title, author, path)


@app.route("/sitemaps")
def sitemaps():
    return render_template("sitemap.xml")


@app.route("/robots.txt")
def robots():
    return render_template("robots.txt")


# SPECIAL PAGES -------------------------------------------------------------------------------------------------------+
@app.route("/hackers/code=8059<date>")
def hackers(date):
    current_date = datetime.datetime.now().strftime("%d%m")
    if date == current_date:
        return render_template(
            "hackers.html",
            version="v" + version,
            copyright="Perseus",
        )
    else:
        title = "Page Not Found"
        author = "harshal"
        path = "errors/404.html"
        return render(title, author, path)


@app.route("/xperiment")
def xperiment_page():
    title = "Xperiment"
    author = "Harshal"
    path = "templates/xperiment/xperiment.html"
    return render(title, author, path)


@app.route("/xperiment/<lab>")
def xperiment(lab):
    try:
        return render_template(
            f"xperiment/{lab}.html",
            path=f"xperiment/{lab}",
            title=lab,
            copyright="Author Write",
        )
    except TemplateNotFound:
        return render_template("xperiment/xperiment.html")


# RUNNING PROGRAM
if __name__ == "__main__":
    clear_logs()
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    init_checkpoint = (
        "@ " + str(datetime.datetime.now()) + " check: server initialized\n"
    )
    with open("logs/main.log", "a") as log:
        log.write(init_checkpoint)
    print(init_checkpoint)
    try:
        app.run(port=port_number)
    except OSError:
        app.run(port=0)
    close_checkpoint = (
        "@ " + str(datetime.datetime.now()) + " check: server terminated\n"
    )
    with open("logs/main.log", "a") as log:
        log.write(close_checkpoint)
        print(close_checkpoint)
