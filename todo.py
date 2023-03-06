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

cursor = connection.cursor()

cursor.execute("SELECT * FROM `Todos` ")

result = cursor.fetchall()

print(result)

 


    