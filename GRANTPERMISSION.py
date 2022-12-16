import psycopg2


conn = psycopg2.connect(
        port = "3200",
        host="139.147.231.99",
        database="errornotfounddb",
        user="yesenia",
        password="")

tableNames = [ "StudentInfo", "Degree", "DegreeRequirements", "Course", "Product", "CoursesTaken", "Staff", "Contacts", "FinancialAid", "Borrow", "ResidenceHall", "Room", "Clubs", "Membership", "Library"]
users = ["joshuagarcia", "pc", "huico"]

def grant_perm():
    """Grants all the users in the ERRORNOTFOUND server access to select, insert, update and delete"""

    cur = conn.cursor()
    for x in tableNames:
        for u in users:
            granting = "GRANT SELECT, INSERT, UPDATE, DELETE ON %s TO %s;" %(x, u)
            cur.execute(granting)
            conn.commit()

    cur.close()
    conn.close()
