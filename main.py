import psycopg2
from CREATE import *
from DROPTABLES import *
from INSERT import *

# THIS FILE WILL RUN THE SIMULATION COMMANDS

if __name__ == '__main__':
    tableNames = [ "StudentInfo", "Degree", "DegreeRequirements", "Course", "Product", "CoursesTaken", "Staff", "Contacts", "FinancialAid", "Borrow"]
    create_tables() 
    #delete_tables(tableNames)
    #insert()
    readCSV()