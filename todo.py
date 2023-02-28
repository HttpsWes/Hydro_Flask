from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/todo")
def index():
    return render_template(
        "todo.html.jinja",
        my_variable="Full cowling!!!",
        list= ["skydiving","Ear-piercings", ]
    )
@app.route("/add", methods=['POST'])
def add():
    new_todo= request.form['new_todo']
    return new_todo


    