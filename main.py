import psycopg2
from CREATE import *
from DROPTABLES import *
from INSERT import *
from GRANTPERMISSION import *
from SELECT import *
from SIMULATION import *

# THIS FILE WILL RUN THE SIMULATION COMMANDS
def setup(tableNames):
    """Sets up all the information we have as well as update information for each student in the necessary tables"""

    delete_tables(tableNames)
    create_tables()
    grant_perm()
    insertAll()
    insertStudentAid()
    insertDegreePerStudent()
    insertDegreeREQPerStudent()
    insertClubMembership()

if __name__ == '__main__':
    tableNames = [ "StudentInfo", "Degree", "DegreeRequirements", "Course", "Product", "CoursesTaken", "Staff", "Contacts", "FinancialAid", "Borrow", "ResidenceHall", "Room", "Clubs", "Membership", "Library"]
    setup(tableNames)
    # insertNewStudent()
    # insertDegreePerStudent()
    # insertDegreeREQPerStudent()
    #simulateCoursesTaken(1)
    #insertNewBorrow()
    printTranscript()
    print("SEMESTER 1 DONE!\n")
    simulateCoursesTaken(1)
    print("SEMESTER 2 DONE!\n")
    simulateCoursesTaken(2)
    print("SEMESTER 3 DONE!\n")
    simulateCoursesTaken(3)
    print("SEMESTER 4 DONE!\n")
    simulateCoursesTaken(4)
    print("SEMESTER 5 DONE!\n")
    simulateCoursesTaken(5)
    print("SEMESTER 6 DONE!\n")
    simulateCoursesTaken(6)
    print("SEMESTER 7 DONE!\n")
    simulateCoursesTaken(7)
    print("SEMESTER 8 DONE!\n")
    simulateCoursesTaken(8)
    print("Print graduated transcript")
    printTranscript()
