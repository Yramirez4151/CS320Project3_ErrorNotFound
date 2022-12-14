import psycopg2
from INSERT import *

conn = psycopg2.connect(
        port = "3200",
        host="139.147.192.196",
        database="errornotfounddb",
        user="yesenia",
        password="")

cur = conn.cursor()

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
