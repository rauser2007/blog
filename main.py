from flask import Flask, redirect, url_for
import settings as stg

app = Flask(__name__, static_folder=stg.PATH_STATIC)
app.config["SECRET_KEY"] = stg.SECRET_KEY

@app.route("/")
def index():
    url = url_for("static", "templates/index.html")
    return redirect(url)

@app.route("/post/category")
def post_category():
    return "ТУТ БУДУТЬ КАТЕГОРІЇ ПОСТІВ"

@app.route("/post/view")
def post_view():
    return "ТУТ БУДЕ ПОСТ"

@app.route("/about")
def about():
    return "ТУТ БУДЕ ІНФО ПРО АВТОРА"



app.run(debug=True)