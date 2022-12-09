import psycopg2
import csv

conn = psycopg2.connect(
        port = "3200",
        host="139.147.236.49",
        database="template1",
        user="yesenia",
        password="")
cur = conn.cursor()

#read CSV files and insert
def readCSV():
    #with open("./MOCK_DATA.csv", 'r') as file:
    with open("./testing.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
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