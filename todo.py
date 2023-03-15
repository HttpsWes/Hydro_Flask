from flask import Flask, render_template, request,redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "Wesley": generate_password_hash("hello"),
    "Ihezuo": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    
bucketlist= ["skydiving","Ear-piercings"]

@app.route("/todo")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `Todos`")
    cursor.execute("SELECT * FROM `Todos` ORDER BY `Complete`")
    results = cursor.fetchall()

    return render_template(
        "todo.html.jinja",
        bucketlist=results,
        my_variable="2023"
    )
@app.route("/add", methods=['POST'])
@auth.login_required
def add():
    cursor = connection.cursor()
    
    new_todo= request.form['new_todo']

    cursor.execute(f"INSERT INTO `Todos`(`Description`) VALUES ('{new_todo}') ")
    

    bucketlist.append(new_todo)
    return redirect(('/todo'))

@app.route("/complete", methods = ['POST'])
@auth.login_required
def complete():

    todo_id = request.form ['todo_id']

    cursor = connection.cursor()
    
    cursor.execute(f"UPDATE `Todos` SET `Complete` = 1 WHERE `id` = {todo_id}" )

    return redirect("/todo")





import pymysql
import pymysql.cursors


connection = pymysql.connect(
    host = "10.100.33.60",
    user = "wihezuo",
    password = "225380047",
    database= "wihezuo_",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit = True
)
 


    