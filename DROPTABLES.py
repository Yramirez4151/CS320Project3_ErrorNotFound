import psycopg2

conn = psycopg2.connect(
        port = "3200",
        host="139.147.199.45",
        database="template1",
        user="yesenia",
        password="")

def delete_tables(tableNames):
    
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
    cur = conn.cursor()
    cur.execute(dropTableStmt)

    cur.close()
    conn.commit()
    conn.close()
