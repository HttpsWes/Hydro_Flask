from flask import Flask, render_template, request,redirect


app = Flask(__name__)

bucketlist= ["skydiving","Ear-piercings"]

@app.route("/todo")
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `Todos`")

    results = cursor.fetchall()

    return render_template(
        "todo.html.jinja",
        bucketlist=results
    )
@app.route("/add", methods=['POST'])
def add():
    cursor.execute(f"INSERT INTO `Todo`(`Description`) VALUES ('{Todos}') ")

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

 


    