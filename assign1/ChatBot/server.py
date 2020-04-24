from flask import Flask, request, jsonify
# from chat import *
import sqlite3
import aiml
import db
import os

app = Flask(__name__)

kernel = aiml.Kernel()
folder = 'aiml-en-us-foundation-alice-master'
for f in os.listdir(folder):
    kernel.learn(os.path.join(folder, f))
kernel.learn("basic_chat.aiml")

prev_domain = ""
prev_faculty = ""

with sqlite3.connect("database.db") as conn:
    db.populate_db(conn)
with sqlite3.connect("conversations.db") as conn1:
    conn1.execute('''CREATE TABLE IF NOT EXISTS CONVOS
                    (NAME TEXT      NOT NULL,
                     MSG  CHAR(50),
                     Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);''')

def resp(inp, conn, db, kernel):
    global prev_domain
    global prev_faculty
    res = ""
    res += kernel.respond(inp)
    domain = kernel.getPredicate('domain')
    faculty = kernel.getPredicate('faculty')
    
    if domain and prev_domain!=domain:
        course  = db.get_coursebydomain(conn, domain)
        prof = db.get_profbycourse(conn, course)

        if course=="" or prof=="":
            print(f"\nCourses for this domain are not available. Please choose a different one")
            res += f"\nCourses for this domain are not available. Please choose a different one"
        else:
            print(f"\nYou can take {course} course. {prof} is the faculty for this course.")
            res += f"\nYou can take {course} course. {prof} is the faculty for this course."
        prev_domain = domain

    if faculty and prev_faculty!=faculty:
        course = db.get_coursebyfaculty(conn, faculty)
        if len(course)==0:
            res += "The faculty you mentioned is not available."
            print("The faculty you mentioned is not available.")
        else:
            print(f"\n{faculty} teaches the course {course}. You should take it.")
            res += f"\n{faculty} teaches the course {course}. You should take it."
        prev_faculty = faculty

    return res

@app.route('/', methods=['GET'])
def hello_world():
    print(request)
    return 'Hello, World!'

@app.route('/', methods=['POST'])
def func():
    print(request.form['name'])
    name = request.form['name']
    inp = request.form['msg']
    with sqlite3.connect("database.db") as conn:
        res = resp(inp, conn, db, kernel)

    with sqlite3.connect("conversations.db") as conn:
        conn.execute(f'INSERT INTO CONVOS (NAME, MSG) VALUES ("{name}", "{inp}"), ("Bot", "{res}");')
    
    return res

@app.route('/convos', methods=['GET'])
def get_convos():
    res = ""
    with sqlite3.connect("conversations.db") as conn:
        res = db.show_table(conn, "CONVOS")
    return jsonify(res), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')