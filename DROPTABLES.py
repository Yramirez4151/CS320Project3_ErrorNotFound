import psycopg2

conn = psycopg2.connect(
        port = "3200",
        host="139.147.231.99",
        database="errornotfounddb",
        user="yesenia",
        password="")

def delete_tables(tableNames):
    """Deleres all 15 tables needed for the database from the ERRORNOTFOUND SERVER"""
    
    cur = conn.cursor()
    for x in tableNames:
        #tableName = x
        dropTableStmt = "DROP TABLE %s CASCADE;" %x
        cur.execute(dropTableStmt)
        conn.commit()

    cur.close()
    conn.close()

def delete_table():
    """Deletes StudentInfo from the database in the ERRORNOTFOUND SERVER"""
    tableName = "StudentInfo"
    dropTableStmt = "DROP TABLE %s;" %tableName
    cur = conn.cursor()
    cur.execute(dropTableStmt)

    cur.close()
    conn.commit()
    conn.close()
