import psycopg2

con = psycopg2.connect(
    port = "3200",
    host="localhost",
    database="template1",
    user="yesenia",
    password="")

cur = con.cursor()

cur.execute("CREATE TABLE Persons ( PersonID int, LastName varchar(255), FirstName varchar(255), Address varchar(255), City varchar(255));")

cur.execute("SELECT * FROM Persons;")

cur.execute("INSERT INTO Persons VALUES ( 1, 'Huico', 'Josh', '1619 W North St', 'Chicago');")

print(cur.execute("SELECT * FROM Persons;"))

print(con.closed)
con.close()