from flask import Flask, render_template, request,redirect


app = Flask(__name__)

bucketlist= ["skydiving","Ear-piercings"]

@app.route("/todo")
def index():
    return render_template(
        "todo.html.jinja",
        bucketlist=bucketlist
    )
@app.route("/add", methods=['POST'])
def add():
    new_todo= request.form['new_todo']

    bucketlist.append(new_todo)
    return redirect(('/todo'))

    