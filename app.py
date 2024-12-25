import datetime
import os

from flask import Flask, render_template, redirect, request
from markupsafe import Markup

version = "12024.9.2"
port_number = 47777

app = Flask(__name__)


def clear_logs():
    """
    Clear logs by transferring the contents of the main log file to the history log file.

    The function reads the contents of the main log file (logs/main.log) and appends them
    to the history log file (logs/history.log). After transferring the data, it clears the
    contents of the main log file.

    :raises FileNotFoundError: If either logs/main.log or logs/history.log cannot be found.
    :raises IOError: If there is an issue, reading from or writing to any of the log files.

    :return: None
    """
    if not os.path.exists("logs"):
        print("logs directory does not exist")
        os.makedirs("logs", exist_ok=True)
    elif not os.path.exists("logs/main.log"):
        print("logs/main.log does not exist")
        open("logs/main.log", "w").close()
    elif not os.path.exists("logs/history.log"):
        print("logs/history.log does not exist")
        open("logs/history.log", "w").close()
    with open("logs/main.log", "r") as f:
        main_log = f.read()
    with open("logs/history.log", "a") as f:
        f.write(main_log)
    with open("logs/main.log", "w") as f:
        f.write("")


def render(title, author, path):
    """
    Renders a web page using a provided template and dynamic content. The method retrieves
    HTML content from the specified file path, and if the file is empty, a default error
    page is displayed. The title, author, and content are injected into the template for
    rendering.

    :param title: The title of the page to be displayed.
    :type title: str
    :param author: The author or copyright information of the page.
    :type author: str
    :param path: The relative path to the content file within the "library" directory.
    :type path: str
    :return: Rendered web page as an HTML string.
    :rtype: str
    """
    try:
        content = Markup(open(f"library/{path}").read())
    except FileNotFoundError:
        content = Markup(open(f"library/errors/empty.html").read())
    if content == "":
        content = Markup(open("library/errors/empty.html").read())
    return render_template("page.html", title=title, copyright=author, content=content)


def search_files(query, directory="library"):
    """
    Searches for files containing the specified query string within a given directory. The function
    recursively traverses the directory structure, opens each file, checks its contents, and adds files
    containing the query to the result list.

    :param query: The string to be searched within the files is
    :type query: str
    :param directory: The directory path where the search begins. Defaults to "library"
    :type directory: str
    :return: A list of file paths containing the query string
    :rtype: list
    """
    result_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                if query in f.read():
                    result_files.append(file_path)
    return result_files


# MAIN PAGES ----------------------------------------------------------------------------------------------------------+
@app.route("/")
def home():
    author = "Harshal"
    return render_template("index.html", version=version, copyright=author)


@app.route("/search", methods=["GET", "POST"])
def search():
    author = "Harshal"
    if request.method == "POST":
        search_query = request.form.get("search_query", "").strip()
        if not search_query:
            return render_template("search.html", content="No search query provided.")
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
        return render_template("search.html", copyright=author, content=final_result)
    else:
        return render_template("search.html", copyright=author, content="")


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


@app.route("/contribute/notes")
def contribute_notes():
    title = "Submit Notes"
    author = "Harshal"
    path = "contributions/notes.html"
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
    with open("logs/main.log", "a") as log:
        log.write(error)
    print(error)
    title = "Server Error"
    author = "Harshal"
    path = "errors/500.html"
    return render(title, author, path)


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


if __name__ == "__main__":
    clear_logs()
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
        log.close()
