import psycopg2
from INSERT import *

conn = psycopg2.connect(
        port = "3200",
        host="139.147.231.99",
        database="errornotfounddb",
        user="yesenia",
        password="")

cur = conn.cursor()

def insertNewStudent():
        """Uses user input to add a new student into the StudentInfo table assuming you wouldn't insert a upperclassman"""

        print('Enter new Student LNum')
        LNum = input()
        print('Enter student First Name')
        FName = input()
        print('Enter student Middle Name')
        MName = input()
        print('Enter student Last Name')
        LName = input()
        ClassTitle = "Freshman" #default
        print('Enter student graduation year')
        GradYear = input()
        Email = LName + FName[0] + "@lafayette.edu"
        print('Enter student phone number')
        PhoneNum = input()
        print('Enter students address')
        Address = input()
        print('Enter student Residence Hall')
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
        """ Prints a specific student transcript into terminal """

        print('Enter Student LNum')
        LNum = input()
        postgres_insert_query = """SELECT * FROM CoursesTaken WHERE LNum = %s""" 
        cur.execute(postgres_insert_query, LNum)
        conn.commit()
        courses = cur.fetchall()
        print("CourseID  Term  Status  Grade")
        for row in courses:
                print(row[2],"    ", row[3], " ", row[4]," ", row[6])


def simulate():
        """ updates student class title based on number of experienced semesters """

        for sem in range(8):
                simulateCoursesTaken(sem)
                if sem == 3:
                        postgres_update_query = """UPDATE StudentInfo SET ClassTitle = 'Sophmore' WHERE ClassTitle = 'Freshman'"""
                if sem == 5:
                        postgres_update_query = """UPDATE StudentInfo SET ClassTitle = 'Junior' WHERE ClassTitle = 'Sophmore'"""
                if sem == 7:
                        postgres_update_query = """UPDATE StudentInfo SET ClassTitle = 'Senior' WHERE ClassTitle = 'Junior'"""

def simulateCoursesTaken(sem):
        """ updates student's transcript in CoursesTaken based on the courses takens in a semester  """

        postgres_insert_query = """SELECT LNum, DegreeID FROM Degree""" 
        postgres_select_query = """SELECT CourseID FROM Course"""
        cur.execute(postgres_insert_query)
        conn.commit()
        students = cur.fetchall()
        cur.execute(postgres_select_query)
        conn.commit()
        courseIDs = cur.fetchall()

        Status = "Enrolled"
        Requirement = ""
        Grade = "A"
        Notes = "You're killing this college thing :)"

        if sem == 1:
                x = 1
                y = 5
                TermTaken = "Fall 1"
        elif sem == 2:
                x = 5
                y = 9
                TermTaken = "Spring 1"
        elif sem == 3:
                x = 9
                y = 13
                TermTaken = "Fall 2"
        elif sem == 4:
                x = 13
                y = 17
                TermTaken = "Spring 2"
        elif sem == 5:
                x = 17
                y = 21
                TermTaken = "Fall 3"
        elif sem == 6:
                x = 21
                y = 25
                TermTaken = "Spring 3"
        elif sem == 7:
                x = 25
                y = 29
                TermTaken = "Fall 4"
        elif sem == 8:
                x = 29
                y = 33
                TermTaken = "Spring 4"

        

        for row in students:
                for i in range(x,y):
                        newStudent = [row[0], row[1], courseIDs[i], TermTaken, Status, Requirement, Grade, Notes]
                        insertCoursesTaken(newStudent)