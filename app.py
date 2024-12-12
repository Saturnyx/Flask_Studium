import datetime
import os

from flask import Flask, render_template, redirect, request
from markupsafe import Markup

version = "2024.9"

app = Flask(__name__)
log = open("logs/main.log", 'a')


def clear_logs():
    main_log = open("logs/main.log", 'r')
    history_log = open("logs/history.log", 'a')
    history_log.write(main_log.read())
    main_log = open("logs/main.log", 'w')
    main_log.write('')
    main_log.close()
    history_log.close()


def render(title, author, path):
    content = Markup(open(f"library/{path}").read())
    return render_template("page.html", title=title, copyright=author, content=content)


def search_files(query, directory="library"):
    result_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                if query in f.read():
                    result_files.append(file_path)
    return result_files


@app.route("/")
def home():
    author = "Harshal"
    return render_template("index.html", version=version, copyright=author)


@app.route("/search", methods=["GET", "POST"])
def search():
    author = "Harshal"
    if request.method == "POST":
        search_query = request.form.get("search_query")
        raw_results = search_files(search_query)
        for i in range(len(raw_results)):
            raw_results[i] = raw_results[i].replace("library\\", "")
            raw_results[i] = (
                f'<a href="/{raw_results[i].replace('.html', '')}">{raw_results[i].replace('.html', '')}</a>'
            )
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


# PHYSICAL CHEMISTRY
@app.route("/chemistry/physical_chemistry/physical_chemistry")
def physical_chemistry():
    title = "Physical Chemistry"
    author = "Harshal"
    path = "chemistry/physical_chemistry/physical_chemistry.html"
    return render(title, author, path)


@app.route("/chemistry/physical_chemistry/atoms")
def atoms():
    title = "Atoms"
    author = "Harshal"
    path = "chemistry/physical_chemistry/atoms.html"
    return render(title, author, path)


@app.route("/chemistry/physical_chemistry/periodic_table")
def periodic_table():
    title = "Periodic Table"
    author = "Harshal"
    path = "chemistry/physical_chemistry/periodic_table.html"
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


# ERRORS --------------------------------------------------------------------------------------------------------------+
@app.errorhandler(404)
def page_not_found(e):
    title = "Page Not Found"
    author = "Harshal"
    path = "errors/404.html"
    return render(title, author, path)


@app.errorhandler(400)
def page_not_found(e):
    title = "Bad Request"
    author = "Harshal"
    path = "errors/400.html"
    return render(title, author, path)


@app.errorhandler(500)
def page_not_found(e):
    error = '@ ' + str(datetime.datetime.now()) + ' error: 500 by ' + request.remote_addr + '\n'
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
        return render_template("hackers.html", version=version, copyright='Perseus')
    else:
        title = "Page Not Found"
        author = "harshal"
        path = "errors/404.html"
        return render(title, author, path)


if __name__ == "__main__":
    clear_logs()
    init_checkpoint = '@ ' + str(datetime.datetime.now()) + ' check: server initialized\n'
    log.write(init_checkpoint)
    print(init_checkpoint)
    app.run()
    close_checkpoint = '@ ' + str(datetime.datetime.now()) + ' check: server terminated\n'
    log.write(close_checkpoint)
    print(close_checkpoint)
    log.close()
