import pymysql
import pymysql.cursors


connection = pymysql.connect(
    host = "10.100.33.60",
    user = "wihezuo",
    password = "225380047",
    database= "world",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM `country` ")

result = cursor.fetchall()

print(result[3]['HeadOfState'])
