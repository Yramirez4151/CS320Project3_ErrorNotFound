import psycopg2
from INSERT import *

conn = psycopg2.connect(
        port = "3200",
        host="139.147.231.99",
        database="errornotfounddb",
        user="yesenia",
        password="")

cur = conn.cursor()
degreeID = 1

def insertStudentAid():
        """ updates student's financial aid by giving every student 60K in schollarships, 60K in pell grant, 1K in loans and 2K in work study """

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
        """ updates student's degree in the the degree table by making all students BS CS students with a 4.0 GPA """

        global degreeID
        CumulativeGPA = 4
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
        """ updates student's degree requirments by making every student in Good academic standing, 
        with Professor Pfaffmann as their advisors and requiring 32 credits to finish their degree """

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

def insertClubMembership():
        """ updates student club membershio by putting all students in ACM since they're all CS students """

        ClubID = 1
        Role = "Member"
        Active = "TRUE"
        Forms = "TRUE"
        postgres_insert_query = """SELECT LNum FROM StudentInfo""" 
        cur.execute(postgres_insert_query)
        conn.commit()
        students = cur.fetchall()

        for LNum in students:
            newStudent = [LNum, ClubID, Role, Active, Forms]
            insertMembership(newStudent)

