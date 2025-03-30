import os

from flask import render_template
from markupsafe import Markup


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
        with open(f"library/{path}", "r") as f:
            content = Markup(f.read())
    except FileNotFoundError:
        with open("library/errors/404.html", "r") as f:
            content = Markup(f.read())
    if content == "":
        with open("library/errors/empty.html") as f:
            content = Markup(f.read())
    return render_template(
        "page.html",
        title=title,
        copyright=author,
        content=content,
        path=path.replace(".html", ""),
    )


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
                    if "!" not in file_path:
                        if "xperiment" not in file_path:
                            result_files.append(file_path)
    return result_files
