import psycopg2
from INSERT import *

conn = psycopg2.connect(
        port = "3200",
        host="139.147.192.196",
        database="errornotfounddb",
        user="yesenia",
        password="")

cur = conn.cursor()
degreeID = 1

def insertStudentAid():
        Scholarships = 60000,
        PellGrant = 60000,
        Loans = 1000,
        WorkStudy = 2000,
        postgres_insert_query = """SELECT LNum FROM StudentInfo""" 
        cur.execute(postgres_insert_query)
        conn.commit()
        students = cur.fetchall()

        for LNum in students:
            newStudent = [LNum, Scholarships, PellGrant, Loans, WorkStudy]
            insertFinancialAid(newStudent)

def insertDegreePerStudent():
        global degreeID
        CumulativeGPA = 0
        DegreeID = degreeID
        dType = "BS"
        Major = "CS"
        Minor = " "
        postgres_insert_query = """SELECT LNum FROM StudentInfo""" 
        cur.execute(postgres_insert_query)
        conn.commit()
        students = cur.fetchall()

        for LNum in students:
            newStudent = [LNum, CumulativeGPA, degreeID, dType, Major, Minor]
            insertDegree(newStudent)
            degreeID = degreeID + 1

def insertDegreeREQPerStudent():
        CurrCredits = 0
        CredReq = 32
        Notes = " "
        TransferredCreds = 0
        A_Standing = "Good"
        EnrollmentStat = "Active"
        DroppedCourses = " "
        Advisor = "Pfaffmann"
        Date_started = "FY2022"
        postgres_insert_query = """SELECT DegreeID FROM Degree""" 
        cur.execute(postgres_insert_query)
        conn.commit()
        degrees = cur.fetchall()

        for pair in degrees:
            newStudent = [pair, CurrCredits, CredReq, Notes, TransferredCreds, A_Standing, EnrollmentStat, DroppedCourses, Advisor, Date_started]
            insertDegreeRequirements(newStudent)
