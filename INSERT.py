import psycopg2
import csv

conn = psycopg2.connect(
        port = "3200",
        host="139.147.201.76",
        database="errornotfounddb",
        user="yesenia",
        password="")
cur = conn.cursor()

#read CSV files and insert
def readCSV():
    #with open("./MOCK_DATA.csv", 'r') as file:
    with open("./DATA/StudentInfoData.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertStudent(row)
        cur.close()
        conn.close()

def insert():
    try:
        cur = conn.cursor()
        postgres_insert_query = """ INSERT INTO StudentInfo (LNum, FName, MName, LName, ClassTitle, GradYear, Email, PhoneNum, Address, ResidenceHallID, RoomID, DOB, Enrollmentstatus, POBox, FERPA, SSN, PreferredName, MealPlan, Notes, EmployeeID, ExcelStudent) VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"""
        record_to_insert = (989815820,'Doina', 'Jakub', 'Andrews', 'Freshman', 2032, 'jakubd@lafayette.edu', '412-734-7650','1606 West Drive', 1, 23, '1961-12-09', 'Active', 9965, True, 500089487, 'Yessi', 7,'', 1, False)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def insertStudent(student):
    try:
        postgres_insert_query = """ INSERT INTO StudentInfo (LNum, FName, MName, LName, ClassTitle, GradYear, Email, PhoneNum, Address, ResidenceHallID, RoomID, DOB, Enrollmentstatus, POBox, FERPA, SSN, PreferredName, MealPlan, Notes, EmployeeID, ExcelStudent) VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"""
        record_to_insert = (student)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertDegree(row):
    try:
        postgres_insert_query = """ INSERT INTO Degree (LNum, CumulativeGPA, DegreeID, dType, ClassTitle, Major, Minor) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertDegreeRequirements(row):
    try:
        postgres_insert_query = """ INSERT INTO DegreeRequirements (DegreeID, CurrCredits, CredReq, Notes, TransferredCreds, A_Standing, EnrollmentStat, DroppedCourses, Advisor, Date_started) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertCourse(row):
    try:
        postgres_insert_query = """ INSERT INTO Course (CourseID, Professor, Name, Department) VALUES (%s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertCoursesTaken(row):
    try:
        postgres_insert_query = """ INSERT INTO CoursesTaken (LNum, DegreeID, CourseID, TermTaken, Status, Requirement, Grade, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertProduct(row):
    try:
        postgres_insert_query = """ INSERT INTO Product (ProductID, ProductType, Name) VALUES (%s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertStaff(row):
    try:
        postgres_insert_query = """ INSERT INTO Staff (StaffID, StaffDept, StaffName, Wage, SSN, Role) VALUES (%s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertContacts(row):
    try:
        postgres_insert_query = """ INSERT INTO Contacts (LNum, Ranking_of_importance, Relationship, Name, PhoneNum, Secondary_PhoneNum, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertFinancialAid(aid):
    try:
        postgres_insert_query = """ INSERT INTO FinancialAid (LNum, Scholarships, PellGrant, Loans, WorkStudy) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (aid)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertBorrow(borrow):
    try:
        postgres_insert_query = """ INSERT INTO Borrow (LNum, Lib_Name, ProductID, Date_Borrowed, Due_Date, Date_Returned) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (borrow)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertHall(hall):
    try:
        postgres_insert_query = """ INSERT INTO ResidenceHall (RID, HallName, GreekLife, Location, Tier, InterestGroup, Capacity, Elevators, AC, Coed, Laundry, Kitchen, ResLifeStaff, HR, Accessiblity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (hall)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertBorrow(borrow):
    try:
        postgres_insert_query = """ INSERT INTO Borrow (RoomID, RID, Type, RoomNum, RA, AC, Floor) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (borrow)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertClubs(clubs):
    try:
        postgres_insert_query = """ INSERT INTO Clubs (ClubID, Name, ClubType, Budget, Coach, FacAdvisor, MeetingLoc, Contact, Weblink, Email, Active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (clubs)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertMembership(member):
    try:
        postgres_insert_query = """ INSERT INTO Membership (LNum, ClubID, MembershipInfo, Role, Active, Forms) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (member)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertLibrary(library):
    try:
        postgres_insert_query = """ INSERT INTO Library (Name, TechServices, Collection, Hours, Printer, Events, MaxOccupancy) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (library)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        count = cur.rowcount
        print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)