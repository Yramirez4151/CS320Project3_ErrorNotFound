import psycopg2

conn = psycopg2.connect(
        port = "3200",
        host="139.147.192.196",
        database="errornotfounddb",
        user="yesenia",
        password="")

cur = conn.cursor()

def selectStatement():
        cur = conn.cursor()
        postgres_insert_query = """SELECT column_name FROM information_schema.columns WHERE table_name = 'attribute' ORDER BY ordinal_position"""
        cur.execute(postgres_insert_query)
        conn.commit()
        cur.close()
        conn.close()
