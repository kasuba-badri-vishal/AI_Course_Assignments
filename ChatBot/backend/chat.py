import os
import aiml
import sqlite3
from db import populate_db, show_table, get_coursebydomain, get_profbycourse, get_coursebyfaculty


BRAIN_FILE="brain.dump"
# Create the kernel and learn AIML files

kernel = aiml.Kernel()
kernel.learn("basic_chat.aiml")
# folder = 'aiml-en-us-foundation-alice-master'
# for f in os.listdir(folder):
#     kernel.learn(os.path.join(folder, f))

# if os.path.exists(BRAIN_FILE):
#     print("Loading from brain file: " + BRAIN_FILE)
#     kernel.loadBrain(BRAIN_FILE)
# else:
#     kernel.bootstrap(learnFiles="basic_chat.aiml")
#     print("Saving brain file: " + BRAIN_FILE)
#     kernel.saveBrain(BRAIN_FILE)

# Press CTRL-C to break this loop
conn = sqlite3.connect("database.db")
populate_db(conn)
prev_domain = ""
prev_faculty = ""

while True:
    domain = kernel.getPredicate('domain')
    faculty = kernel.getPredicate('faculty')
    if domain and prev_domain!=domain:
        course = get_coursebydomain(conn, domain)
        prof = get_profbycourse(conn, course)
        print(f"You can take {course} course. {prof} is the faculty for this course.")
        prev_domain = domain
    elif faculty and prev_faculty!=faculty:
        course = get_coursebyfaculty(conn, faculty)
        if len(course)==0:
            print("The faculty you mentioned is not available.")
        else:
            print(f"{faculty} teaches the course {course}. You should take it.")
        prev_faculty = faculty
    else:
        print(kernel.respond(input("Enter your message >> ")))

# Loading database
# show_table(conn, "courses")
# domain = "Software Engineering"
# domain = "DATA"
# course = get_coursebydomain(conn, domain)
# get_profbycourse(conn, course)
conn.close()

def resp(inp):
    # print()
    res = kernel.respond(inp)
    return res