import os

from flask import Flask, render_template, request, redirect
from markupsafe import Markup

version = "10.5"

app = Flask(__name__)


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
def home():  # put application's code here
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
                f'<a href="/{raw_results[i].replace('.html','')}">{raw_results[i].replace('.html','')}</a>'
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

if __name__ == "__main__":
    app.run()
