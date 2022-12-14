import psycopg2
from INSERT import *

conn = psycopg2.connect(
        port = "3200",
        host="139.147.192.196",
        database="errornotfounddb",
        user="yesenia",
        password="")

cur = conn.cursor()

def insertNewStudent():
    print('Enter new Student LNum')
    LNum = input()
    print('Enter student First Name')
    FName = input()
    print('Enter student Middle Name')
    MName = input()
    print('Enter student Last Name')
    LName = input()
    ClassTitle = "First Year" #default
    print('Enter student graduation year')
    GradYear = input()
    Email = LName + FName[0] + "@lafayette.edu"
    print('Enter student phone number')
    PhoneNum = input()
    print('Enter students address')
    Address = input()
    print('Enter student Residence Hall (1-10)')
    ResidenceHallID = input()
    print('Enter student roomid')
    RoomID = input()
    print('Enter student date of birth')
    DOB = input()
    print('Enter student enrollment status')
    Enrollmentstatus = input()
    print('Enter student POBox')
    POBox = input()
    print('Did student complete FERPA? enter TRUE if yes, FALSE if no')
    FERPA = input()
    print('Enter student SSN')
    SSN = input()
    print('Enter student preferred name')
    PreferredName = input()
    print('Enter student meal plan. (7,14 or 24)')
    MealPlan = input()
    Notes = " " #default
    print('Enter student unique employee ID')
    EmployeeID = input()
    print('Is student in EXCEL? enter TRUE if yes, FALSE if no')
    ExcelStudent = input()
    student = [LNum, FName, MName, LName, ClassTitle, GradYear, Email, PhoneNum, Address, ResidenceHallID, RoomID, DOB, Enrollmentstatus, POBox, FERPA, SSN, PreferredName, MealPlan, Notes, EmployeeID, ExcelStudent]
    insertStudent(student)
    # print('FROM WHERE:')
    # table = input()

def printTranscript():
        print('Enter Student LNum')
        LNum = input()
        postgres_insert_query = """SELECT * FROM CoursesTaken WHERE LNum = %s""" 
        cur.execute(postgres_insert_query, LNum)
        conn.commit()
        courses = cur.fetchall()
        print("CourseID  Term  Status  Grade")
        for row in courses:
                print(row[2],"    ", row[3], " ", row[4]," ", row[6])