import psycopg2

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
        )
    #conn = None
    conn = psycopg2.connect(
            port = "3200",
            host="139.147.207.184",
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
            host="139.147.207.184",
            database="template1",
            user="yesenia",
            password="")
    
    cur = conn.cursor()
    for x in tableNames:
        #tableName = x
        dropTableStmt = "DROP TABLE %s CASCADE;" %x
        cur.execute(dropTableStmt);
        conn.commit()

    cur.close()
    conn.close()

def delete_table():
    tableName = "StudentInfo"
    dropTableStmt = "DROP TABLE %s;" %tableName
    conn = psycopg2.connect(
            port = "3200",
            host="139.147.207.184",
            database="template1",
            user="yesenia",
            password="")

    cur = conn.cursor()
    cur.execute(dropTableStmt)

    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    tableNames = [ "vendors", "part_drawings", "parts", "vendor_parts"]
    create_tables() 
    delete_tables(tableNames)