import psycopg2
from CREATE import *
from DROPTABLES import *
from INSERT import *
from GRANTPERMISSION import *
from SELECT import *
from SIMULATION import *

# THIS FILE WILL RUN THE SIMULATION COMMANDS
def setup(tableNames):
    delete_tables(tableNames)
    create_tables()
    grant_perm()
    insertAll()
    insertStudentAid()
    insertDegreePerStudent()
    insertDegreeREQPerStudent()


if __name__ == '__main__':
    tableNames = [ "StudentInfo", "Degree", "DegreeRequirements", "Course", "Product", "CoursesTaken", "Staff", "Contacts", "FinancialAid", "Borrow", "ResidenceHall", "Room", "Clubs", "Membership", "Library"]
    #setup(tableNames)
    # insertNewStudent()
    # printTranscript()
    insertClubMembership()