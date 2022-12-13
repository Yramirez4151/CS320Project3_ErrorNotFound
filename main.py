import psycopg2
from CREATE import *
from DROPTABLES import *
from INSERT import *
from GRANTPERMISSION import *

# THIS FILE WILL RUN THE SIMULATION COMMANDS


if __name__ == '__main__':
    tableNames = [ "StudentInfo", "Degree", "DegreeRequirements", "Course", "Product", "CoursesTaken", "Staff", "Contacts", "FinancialAid", "Borrow", "ResidenceHall", "Room", "Clubs", "Membership", "Library"]
    delete_tables(tableNames)
    create_tables()
    grant_perm()
    #readStudentCSV()
    #readLibraryCSV()
    #readHallCSV()
    #readRoomCSV()
    #readProductCSV()
    #readCourseCSV()
    #readStaffCSV()
    #readContactCSV()
    insertAll()
