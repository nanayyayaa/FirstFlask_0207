from flask import Flask
#from markupsafe import escape
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!"
@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    post_id=post_id+10
    return f"Post #{post_id}"


