def populate_db(conn):
    conn.execute('''DROP TABLE  IF EXISTS FACULTY;''')
    conn.execute('''DROP TABLE  IF EXISTS COURSES;''')
    conn.execute('''DROP TABLE  IF EXISTS TRENDING;''')

    conn.execute('''CREATE TABLE IF NOT EXISTS FACULTY
                (FID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL,
                DEPARTMENT     CHAR(50));''')
    conn.execute('''CREATE TABLE IF NOT EXISTS COURSES
                    (CID INT PRIMARY KEY     NOT NULL,
                    COURSE_NAME     TEXT    NOT NULL,
                    DEPARTMENT      char(50),
                    DOMAIN     TEXT    NOT NULL,
                    FID INT NOT NULL);''')
    conn.execute('''INSERT INTO FACULTY
                    (FID,    NAME,    DEPARTMENT) VALUES
                    (401,   "Jason Blake", "CSE"),
                    (402,   "Phil Morgan", "CSE"),
                    (403,   "Connor Clarkson", "CSE"),
                    (404,   "Alan King", "ECE"),
                    (405,   "Dominic Greene", "ECE"),
                    (406,   "Ryan Reid", "EEE"),
                    (407,   "Nicholas Mitchell", "EEE"),
                    (408,   "Jonathan Martin", "CIVIL"),
                    (409,   "Jake Langdon", "CIVIL"),
                    (410,   "Carolyn Harris", "MECH"),
                    (411,   "Andrea Watson", "MECH"),
                    (412,   "Felicity Dowd", "BIOT"),
                    (413,   "Natalie Sharp", "BIOT"),
                    (414,   "Kylie Edmunds", "MANU"),
                    (415,   "Julia McLean", "CHEM");''')
    conn.execute('''INSERT INTO COURSES
                    (CID,  COURSE_NAME,                DEPARTMENT, DOMAIN,  FID) VALUES
                    (101, "Foundation of Data Science"     , "CSE", "Data Science" ,401),
                    (102, "Machine Learning"               , "CSE", "Data Science"  ,401),
                    (103, "Data Mining"                    , "CSE", "Data Science"  ,402),
                    (104, "Information Retrieval"          , "CSE", "Data Science"  ,401),
                    (105, "Software Engineering"           , "CSE", "Software Eng"  ,402),
                    (106, "Computational Geometry"         , "CSE", "Math" ,403),
                    (107, "Computer Graphics"              , "CSE", "Image processing",403),
                    (108, "Cloud Computing"                , "CSE", "Cloud Technology",402),
                    (109, "Cryptography"                   , "CSE", "Computer Security",403),
                    (110, "Artificial Intelligence"        , "CSE", "Data Science",403),
                    (116, "Introduction to Bioinformatics" ,"BIOT", "Bio Technology" ,412),
                    (117, "Genomics"                       ,"BIOT", "Bio Technology" ,413),
                    (118, "Introduction to Nanoscience"    ,"CHEM", "Chemistry" ,415),
                    (119, "Microfluidics and its application","CHEM", "Chemistry" ,415),
                    (120, "Computational Geomechanics"      , "CIVIL", "Civil" ,408),
                    (121, "Introduction to Bridge Engineering", "CIVIL", "Civil" ,409),
                    (122, "Communication Networks"         , "EEE", "Communications" , 406),
                    (123, "Digital Communication"          , "EEE",  "Communications" ,406),
                    (124, "Satellite Communication"        , "ECE", "Communications" , 403),
                    (125, "Advanced Metal Forming"         , "MANU", "Manufacturing" , 414),
                    (126, "Supply Chain Management"        , "MANU", "Manufacturing" , 414),
                    (127, "Product Design"                 , "MECH", "Mechanical" , 410),
                    (128, "Power Plant Engineering"        , "MECH", "Mechanical" ,410);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS TRENDING
                (RANK INT PRIMARY KEY     NOT NULL,
                DOMAIN           TEXT    NOT NULL);''')
    conn.execute('''INSERT INTO TRENDING
                (RANK, DOMAIN) VALUES
                (1, "Data Science"),
                (2, "Cloud Technology"),
                (3, "Software Eng"),
                (4, "Computer Security"),
                (5, "Communications"),
                (6, "Image Processing"),
                (7, "Bio Technology"),
                (8, "Chemistry"),
                (9, "Math"),
                (10, "Civil"),
                (11, "Manufacturing"),
                (12, "Mechanical");''')

def domain_mapping(domain):
    domain = domain.lower()
    if "data" in domain:
        return "data science"
    if "software" in domain:
        return "software engineering"
    if "math" in domain:
        return "math"
    if ("image" in domain) or ("processing" in domain):
        return "image processing"
    if ("electronic" in domain) or  ("electronic" in domain):
        return "communications"
    if ("electrical" in domain):
        return "eee"
    if ("manu" in domain):
        return "manufacturing"
    if ("civil" in domain):
        return "civil"
    if ("chem" in domain):
        return "chemistry"
    if ("bio" in domain):
        return "bio technology"
    if ("cloud" in domain):
        return "cloud technology"
    if ("security" in domain):
        return "computer security"

    return ""
    

def show_table(conn, table_name):
    res = ""
    curr = conn.cursor()
    curr.execute(f"SELECT * FROM {table_name};")
    tab = curr.fetchall()
    for row in tab:
        print(row)
        res += (row[0] + ", " + row[1] + ", " + row[2] + "\n")
    # return res
    return tab

def get_coursebydomain(conn, domain):
    curr = conn.cursor()
    curr.execute(f"SELECT DOMAIN FROM TRENDING;")
    tab = curr.fetchall()
    for row in tab:
        if (domain.lower() in row[0].lower()) or (row[0].lower() in domain.lower()) or (domain_mapping(domain) in row[0].lower()):
            domain = row[0].lower()

    course = ""
    curr = conn.cursor()
    curr.execute(f"SELECT COURSE_NAME FROM COURSES, TRENDING WHERE LOWER(TRENDING.DOMAIN) like '{domain.lower()}' AND COURSES.DOMAIN=TRENDING.DOMAIN;")
    tab = curr.fetchall()
    if len(tab)>0:
        course = tab[0][0]
    # print(course)
    return course

def get_profbycourse(conn, course):
    prof = ""
    curr = conn.cursor()
    curr.execute(f"SELECT NAME FROM FACULTY, COURSES WHERE FACULTY.FID=COURSES.FID AND COURSES.COURSE_NAME='{course}';")
    tab = curr.fetchall()
    if len(tab)>0:
        prof = tab[0][0]
    # print(prof)
    return prof

def get_coursebyfaculty(conn, faculty):
    curr = conn.cursor()
    curr.execute(f"SELECT NAME FROM FACULTY;")
    tab = curr.fetchall()
    for row in tab:
        if (faculty.lower() in row[0].lower()) or (row[0].lower() in faculty.lower()):
            faculty = row[0]

    course = ""
    curr = conn.cursor()
    curr.execute(f"SELECT COURSE_NAME FROM FACULTY, COURSES WHERE FACULTY.FID=COURSES.FID AND FACULTY.NAME='{faculty}';")
    tab = curr.fetchall()
    if len(tab)>0:
        course = tab[0][0]
    # print(prof)
    return course
