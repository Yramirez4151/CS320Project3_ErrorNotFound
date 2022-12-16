import psycopg2
import csv
from configwriter import *

conn = psycopg2.connect(
        port = "3200",
        host="139.147.231.99",
        database="errornotfounddb",
        user="yesenia",
        password="")

cur = conn.cursor()

#read CSV files and insert
def readStudentCSV():
    """ Reads from a csv file filled with freshman students and inserts them into the StudentInfo Table"""
    with open("./DATA/Freshman.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertStudent(row)

def insertStudent(student):
    """ takes in a student parameter to insert that student into the StudentInfo table"""

    try:
        postgres_insert_query = """ INSERT INTO StudentInfo (LNum, FName, MName, LName, ClassTitle, GradYear, Email, PhoneNum, Address, ResidenceHallID, RoomID, DOB, Enrollmentstatus, POBox, FERPA, SSN, PreferredName, MealPlan, Notes, EmployeeID, ExcelStudent) VALUES (%s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"""
        record_to_insert = (student)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

# def readDegreeCSV():
#     with open("./DATA/DegreeData.csv", 'r') as file:
#         csvreader = csv.reader(file)
#         for row in csvreader:
#             # print(row)
#             insertDegree(row)

def insertDegree(row):
    """ takes in a student's degree input to insert that degree info into the Degreee table"""

    try:
        postgres_insert_query = """ INSERT INTO Degree (LNum, CumulativeGPA, DegreeID, dType, Major, Minor) VALUES (%s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

# def readDegreeReqCSV():
#     #with open("./MOCK_DATA.csv", 'r') as file:
#     with open("./DATA/StudentInfoData.csv", 'r') as file:
#         csvreader = csv.reader(file)
#         for row in csvreader:
#             # print(row)
#             insertStudent(row)

def insertDegreeRequirements(row):
    """ takes in a row parameter to insert that new degree requirment into the DegreeRequirments table"""

    try:
        postgres_insert_query = """ INSERT INTO DegreeRequirements (DegreeID, CurrCredits, CredReq, Notes, TransferredCreds, A_Standing, EnrollmentStat, DroppedCourses, Advisor, Date_started) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readCourseCSV():
    """ Reads from the courses.csv file to insert the available courses into the course table"""

    with open("./DATA/courses.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertCourse(row)

def insertCourse(course):
    """ takes in a course parameter to insert that new course into the Course table"""

    try:
        postgres_insert_query = """ INSERT INTO Course (CourseID, Professor, Name, Department) VALUES (%s, %s, %s, %s)"""
        record_to_insert = (course)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

# def readCourseTaken():
#     with open("./DATA/StudentInfoData.csv", 'r') as file:
#         csvreader = csv.reader(file)
#         for row in csvreader:
#             # print(row)
#             insertStudent(row)

def insertCoursesTaken(row):
    """ takes in a row parameter to insert that new course the student took  into the coursesTaken table"""

    try:
        postgres_insert_query = """ INSERT INTO CoursesTaken (LNum, DegreeID, CourseID, TermTaken, Status, Requirement, Grade, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readProductCSV():
    """ Reads from the productData csv to insert into the Product table"""

    with open("./DATA/ProductData.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            insertProduct(row)

def insertProduct(row):
    """ takes in a row parameter to insert that new product into the Product table"""

    try:
        postgres_insert_query = """ INSERT INTO Product (ProductID, ProductType, Name) VALUES (%s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readStaffCSV():
    """ Reads from the StaffData csv file and inserts into the Staff table"""

    with open("./DATA/StaffData.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertStaff(row)

def insertStaff(row):
    """ takes in a row parameter to insert a new staff member into the Staff table"""

    try:
        postgres_insert_query = """ INSERT INTO Staff (StaffID, StaffDept, StaffName, Wage, SSN, Role) VALUES (%s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readContactCSV():
    """ Reads the ContactData csv file and inserts the contacts into the Contacts table"""

    with open("./DATA/ContactData.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertContacts(row)

def insertContacts(row):
    """ takes in a row parameter to insert a new contact into the Contacts table"""

    try:
        postgres_insert_query = """ INSERT INTO Contacts (LNum, Ranking_of_importance, Relationship, Name, PhoneNum, Secondary_PhoneNum, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (row)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def insertFinancialAid(aid):
    """ takes in a aid parameter to insert financial aid record for a student"""

    try:
        postgres_insert_query = """ INSERT INTO FinancialAid (LNum, Scholarships, PellGrant, Loans, WorkStudy) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (aid)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

# def readBorrowCSV():
#     """ takes in a row parameter to insert that new degree requirment into the DegreeRequirments table"""
#     #with open("./MOCK_DATA.csv", 'r') as file:
#     with open("./DATA/StudentInfoData.csv", 'r') as file:
#         csvreader = csv.reader(file)
#         for row in csvreader:
#             # print(row)
#             insertStudent(row)

def insertBorrow(borrow):
    """ takes in a borrow parameter to insert that new borrowed item into the Borrow table"""

    try:
        postgres_insert_query = """ INSERT INTO Borrow (LNum, Lib_Name, ProductID, Date_Borrowed, Due_Date, Date_Returned) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (borrow)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readHallCSV():
    """ Reads in the ResidenceHallID csv file to insert it into the ResidenceHall table"""

    with open("./DATA/ResidenceHallID.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertHall(row)

def insertHall(hall):
    """ takes in a hall parameter to insert a hall record into the ResidenceHall table"""

    try:
        postgres_insert_query = """ INSERT INTO ResidenceHall (RID, HallName, GreekLife, Location, Tier, InterestGroup, Capacity, Elevators, AC, Coed, Laundry, Kitchen, ResLifeStaff, HR, Accessibility) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (hall)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readRoomCSV():
    """ Reads in the RoomData csv file to insert it into the Room table"""

    with open("./DATA/RoomData.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            #print(row)
            insertRoom(row)

def insertRoom(room):
    """ takes in a room parameter to insert a room record into the Room table, distinguishing rooms by RoomID and RID"""

    try:
        postgres_insert_query = """ INSERT INTO Room (RoomID, RID, Type, RoomNum, RA, AC, Floor) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (room)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readClubsCSV():
    """ Reads in the clubs csv file to insert it into the Clubs table"""

    with open("./DATA/clubs.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertClubs(row)

def insertClubs(clubs):
    """ takes in a club parameter to insert a club record into the Clubs table"""

    try:
        postgres_insert_query = """ INSERT INTO Clubs (ClubID, Name, ClubType, Budget, Coach, FacAdvisor, MeetingLoc, Contact, Weblink, Email, Active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (clubs)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

# def readMemberCSV():
#     #with open("./MOCK_DATA.csv", 'r') as file:
#     with open("./DATA/StudentInfoData.csv", 'r') as file:
#         csvreader = csv.reader(file)
#         for row in csvreader:
#             # print(row)
#             insertStudent(row)

def insertMembership(member):
    """ takes in a member parameter to insert a member record into the Membership table"""

    try:
        postgres_insert_query = """ INSERT INTO Membership (LNum, ClubID, Role, Active, Forms) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (member)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

def readLibraryCSV():
    """ Reads in the Library csv file to insert it into the Library table"""

    with open("./DATA/LibraryData.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # print(row)
            insertLibrary(row)

def insertLibrary(library):
    """ takes in a library parameter to insert a library record into the Library table"""

    try:
        postgres_insert_query = """ INSERT INTO Library (Name, TechServices, Collection, Hours, Printer, Events, MaxOccupancy) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (library)
        cur.execute(postgres_insert_query, record_to_insert)

        conn.commit()
        # count = cur.rowcount
        # print(count, "Record inserted successfully into vendor")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error) 


def insertAll():
    """ inserts all the csv files that have been collected to initialize data on campus life"""
    
    readStudentCSV()
    readProductCSV()
    readStaffCSV()
    readContactCSV()
    readHallCSV()
    readRoomCSV()
    readClubsCSV()
    readLibraryCSV()
    readCourseCSV()
    # cur.close()
    # conn.close()
