from flask_app import app

from flask import render_template , redirect , request

from flask_app.models.user import User

@app.route("/")
def read():
    user = User.get_all()
    return render_template("readall.html",users=user)

@app.route("/users", methods=["POST"])
def create():
    User.create(request.form)
    return redirect ("/")

@app.route("/newuser",methods=["POST"] )
def createNew():
    return render_template ("create.html")