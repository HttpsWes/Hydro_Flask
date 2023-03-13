from flask import Flask, render_template, request,redirect


app = Flask(__name__)

bucketlist= ["skydiving","Ear-piercings"]

@app.route("/todo")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `Todos`")
    cursor.execute("SELECT * FROM `Todos` ORDER BY `Complete`")
    results = cursor.fetchall()

    return render_template(
        "todo.html.jinja",
        bucketlist=results
    )
@app.route("/add", methods=['POST'])
def add():
    cursor = connection.cursor()
    
    new_todo= request.form['new_todo']

    cursor.execute(f"INSERT INTO `Todos`(`Description`) VALUES ('{new_todo}') ")
    

    bucketlist.append(new_todo)
    return redirect(('/todo'))

@app.route("/complete", methods = ['POST'])
def complete():

    todo_id = request.form ['todo_id']

    cursor = connection.cursor()
    
    cursor.execute(f"UPDATE `Todos` SET `Complete` = 1 WHERE `id` = {todo_id}" )

    return redirect("/")


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
 


    