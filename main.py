from flask import Flask, redirect, url_for, render_template, request
import settings as stg
import db_scripts as db

app = Flask(__name__, static_folder=stg.PATH_STATIC)
app.config["SECRET_KEY"] = stg.SECRET_KEY

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html") 

@app.route("/post/category/<category_name>")
def post_category(category_name):
    category_id = db.getIdByCategory(category_name) 

    if request.method == "GET":
        posts = db.getPostsByCategory(category_name)

    return render_template("post_category.html", category_name=category_name, category_id=category_id, posts=posts)

    



@app.route("/post/view")
def post_view():
    return "ТУТ БУДЕ ПОСТ"

@app.route("/about")
def about():
    user = db.getUser()
    print(user)
    return render_template("about.html", user=user)



app.run(debug=True)