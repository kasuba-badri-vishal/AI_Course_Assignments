import os
import aiml
import sqlite3


BRAIN_FILE="brain.dump"
# Create the kernel and learn AIML files

kernel = aiml.Kernel()
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
kernel.learn("basic_chat.aiml")

# Press CTRL-C to break this loop
# while True:
#     print(kernel.respond(input("Enter your message >> ")))

conn = sqlite3.connect("database.db")
conn.execute('''CREATE TABLE IF NOT EXISTS FACULTY
                (FID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL,
                DEPARTMENT     CHAR(50));''')
conn.execute('''CREATE TABLE IF NOT EXISTS COURSES
                (CID INT PRIMARY KEY     NOT NULL,
                COURSE_NAME     TEXT    NOT NULL,
                DEPARTMENT      char(50),
                FID INT NOT NULL);''')
conn.execute('''INSERT INTO FACULTY
                (FID,    NAME,    DEPARTMENT) VALUES
                (401,   "Jason	Blake", "CSE"),
                (402,   "Phil	Morgan", "CSE"),
                (403,   "Connor	Clarkson", "CSE"),
                (404,   "Alan	King", "ECE"),
                (405,   "Dominic	Greene", "ECE"),
                (406,   "Ryan	Reid", "EEE"),
                (407,   "Nicholas	Mitchell", "EEE"),
                (408,   "Jonathan	Martin", "CIVIL"),
                (409,   "Jake	Langdon", "CIVIL"),
                (410,   "Carolyn	Harris", "MECH"),
                (411,   "Andrea	Watson", "MECH"),
                (412,   "Felicity	Dowd", "BIOT"),
                (413,   "Natalie	Sharp", "BIOT"),
                (414,   "Kylie	Edmunds", "MANU"),
                (415,   "Julia	McLean", "CHEM");''')
conn.execute('''INSERT INTO COURSES
                (CID,  COURSE_NAME,                DEPARTMENT,  FID) VALUES
                (101, "Foundation of Data Science"     , "CSE", 401),
                (102, "Machine Learning"               , "CSE", 401),
                (103, "Data Mining"                    , "CSE", 402),
                (104, "Information Retrieval"          , "CSE", 401),
                (105, "Software Engineering"           , "CSE", 402),
                (106, "Computational Geometry"         , "CSE", 403),
                (107, "Computer Graphics"              , "CSE", 403),
                (108, "Cloud Computing"                , "CSE", 402),
                (109, "Cryptography"                   , "CSE", 403),
                (110, "Artificial Intelligence"        , "CSE", 403),
                (116, "Introduction to Bioinformatics" , "BIOT",412),
                (117, "Genomics"                       , "BIOT",413),
                (118, "Introduction to Nanoscience"    , "CHEM",415),
                (119, "Microfluidics and its application", "CHEM",415),
                (120, "Computational Geomechanics"      , "CIVIL",408),
                (121, "Introduction to Bridge Engineering", "CIVIL",409),
                (122, "Communication Networks"         , "EEE", 406),
                (123, "Digital Communication"          , "EEE", 406),
                (124, "Satellite Communication"        , "ECE", 403),
                (125, "Advanced Metal Forming"         , "MANU", 414),
                (126, "Supply Chain Management"        , "MANU", 414),
                (127, "Product Design"                 , "MECH", 410),
                (128, "Power Plant Engineering"        , "MECH", 410);''')

                # (111, "Parallel Computing"             , "CSE"),
                # (112, "Network Programming"            , "CSE"),
                # (113, "Neural Networks and Fuzzy Logic", "CSE"),
                # (114, "Cryptography"                   , "CSE"),
                # (115, "Image Processing"               , "CSE"),
conn.close()

def resp(inp):
    return kernel.respond(inp)