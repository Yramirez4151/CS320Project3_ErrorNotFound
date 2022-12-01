import psycopg2

con = psycopg2.connect(
    port = "3200",
    host="139.147.200.35",
    database="template1",
    user="yesenia",
    password="")

cur = con.cursor()

# cur.execute("CREATE TABLE Persons ( PersonID int );")

# cur.execute("SELECT * FROM Persons;")

# cur.execute("INSERT INTO Persons VALUES ( 1 );")

# print(cur.execute("SELECT * FROM Persons;"))

print(con.closed)
con.close()