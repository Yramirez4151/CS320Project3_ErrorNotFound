import psycopg2
from CREATE import *
from DROPTABLES import *
from INSERT import *
from GRANTPERMISSION import *

# THIS FILE WILL RUN THE SIMULATION COMMANDS

if __name__ == '__main__':
    tableNames = [ "StudentInfo", "Degree", "DegreeRequirements", "Course", "Product", "CoursesTaken", "Staff", "Contacts", "FinancialAid", "Borrow", "ResidenceHall", "Room", "Clubs", "Membership", "Library"]
    #create_tables() 
    #grant_perm()
    #delete_tables(tableNames)
    #insert()
    #readCSV()