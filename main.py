import psycopg2

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE StudentInfo (
            LNum INTEGER UNIQUE NOT NULL,
            FName VARCHAR(50) NOT NULL,
            MName VARCHAR(50),
            LName VARCHAR(50) NOT NULL,
            ClassTitle VARCHAR(7),
            GradYear INTEGER NOT NULL,
            Email VARCHAR(50) NOT NULL,
            PhoneNum INTEGER, 
            Address VARCHAR(50) NOT NULL,
            ResidenceHallID INTEGER,
            RoomID INTEGER,
            DOB DATE NOT NULL,
            Enrollmentstatus VARCHAR(50),
            POBox INTEGER,
            FERPA BOOLEAN NOT NULL, 
            SSN INTEGER UNIQUE, 
            PreferredName VARCHAR(50),
            MealPlan INTEGER,
            Notes VARCHAR(100),
            EmployeeID INTEGER, 
            ExcelStudent BOOLEAN,
            PRIMARY KEY (LNum)
            )
        """,
        """
        CREATE TABLE Degree (
            LNum INTEGER NOT NULL,
            CumulativeGPA INTEGER NOT NULL,
            DegreeID INTEGER UNIQUE NOT NULL,
            dType VARCHAR(2) NOT NULL,
            Major VARCHAR(10) NOT NULL,
            Minor VARCHAR(10),
            PRIMARY KEY (LNum, DegreeID, Major),
                FOREIGN KEY(LNum) 
                    REFERENCES StudentInfo(LNum)
            )
        """, 
        """
        CREATE TABLE DegreeRequirements (
            DegreeID INTEGER UNIQUE NOT NULL, 
            CurrCredits INTEGER NOT NULL,
            CredReq INTEGER NOT NULL,
            Notes VARCHAR(200),
            TransferredCreds INTEGER,
            A_Standing VARCHAR(20) NOT NULL,
            EnrollmentStat VARCHAR(20) NOT NULL,
            DroppedCourses VARCHAR(200),
            Advisor VARCHAR(20) NOT NULL,
            Date_started VARCHAR(30) NOT NULL,
            PRIMARY KEY (DegreeID),
                FOREIGN KEY(DegreeID) 
                    REFERENCES Degree(DegreeID)
            )
        """
        )
    #conn = None
    conn = psycopg2.connect(
            port = "3200",
            host="139.147.193.233",
            database="template1",
            user="yesenia",
            password="")

    try:
        # read the connection parameters
        cur = conn.cursor()

        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def delete_tables(tableNames):
    conn = psycopg2.connect(
            port = "3200",
            host="139.147.193.233",
            database="template1",
            user="yesenia",
            password="")
    
    cur = conn.cursor()
    for x in tableNames:
        #tableName = x
        dropTableStmt = "DROP TABLE %s CASCADE;" %x
        cur.execute(dropTableStmt)
        conn.commit()

    cur.close()
    conn.close()

def delete_table():
    tableName = "StudentInfo"
    dropTableStmt = "DROP TABLE %s;" %tableName
    conn = psycopg2.connect(
            port = "3200",
            host="139.147.193.233",
            database="template1",
            user="yesenia",
            password="")

    cur = conn.cursor()
    cur.execute(dropTableStmt)

    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    tableNames = [ "StudentInfo", "Degree", "DegreeRequirements"]
    #create_tables() 
    delete_tables(tableNames)