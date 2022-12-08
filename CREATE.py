import psycopg2

conn = psycopg2.connect(
        port = "3200",
        host="139.147.199.45",
        database="template1",
        user="yesenia",
        password="")

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE StudentInfo (
            LNum INTEGER UNIQUE NOT NULL,
            FName VARCHAR(50) NOT NULL,
            MName VARCHAR(50),
            LName VARCHAR(50) NOT NULL,
            ClassTitle VARCHAR(10),
            GradYear INTEGER NOT NULL,
            Email VARCHAR(200) NOT NULL,
            PhoneNum VARCHAR(15), 
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
        """, 
        """
        CREATE TABLE Course(
            CourseID INTEGER UNIQUE NOT NULL,
            Professor VARCHAR(100),
            Name VARCHAR(200),
            Department VARCHAR(200),
            PRIMARY KEY(CourseID)
            )
        """, 
        """
        CREATE TABLE CoursesTaken (
            LNum INTEGER NOT NULL, 
            DegreeID INTEGER NOT NULL,
            CourseID INTEGER NOT NULL,
            TermTaken VARCHAR(200),
            Status VARCHAR(100),
            Requirement VARCHAR(200),
            Grade VARCHAR(2),
            Notes VARCHAR(200),
            PRIMARY KEY(LNum, DegreeID, CourseID),
                FOREIGN KEY(LNum)
                    REFERENCES StudentInfo(LNum),
                FOREIGN KEY(DegreeID)
                    REFERENCES Degree(DegreeID),
                FOREIGN KEY(CourseID)
                     REFERENCES Course(CourseID)
            )
        """,
        """
        CREATE TABLE Product(
            ProductID INTEGER UNIQUE NOT NULL,
            ProductType VARCHAR(100),
            Name VARCHAR(200),
		    PRIMARY KEY(ProductID)
            )
        """, 
        """
        CREATE TABLE Staff(
            StaffID INTEGER UNIQUE NOT NULL,
            StaffDept VARCHAR(200),
            StaffName VARCHAR(200),
            Wage INTEGER,
            SSN INTEGER,
            Role VARCHAR(200),
            PRIMARY KEY(StaffID)
            )
        """, 
        """
        CREATE TABLE Contacts(
            LNum INTEGER UNIQUE NOT NULL,
            Ranking_of_importance INTEGER,
            Relationship VARCHAR(200),
            Name VARCHAR(200),
            PhoneNum INTEGER,
            Secondary_PhoneNum INTEGER,
            Email VARCHAR(200), 
            PRIMARY KEY(LNum),
                FOREIGN KEY(LNum)
                    REFERENCES StudentInfo(LNum)
            )
        """,
        """
        CREATE TABLE FinancialAid(
            LNum INTEGER UNIQUE NOT NULL,
            Scholarships INTEGER,
            PellGrant INTEGER,
            Loans INTEGER,
            WorkStudy INTEGER,
            PRIMARY KEY(LNum),
                FOREIGN KEY(LNum)
                    REFERENCES StudentInfo(LNum)
            )
        """
        )
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