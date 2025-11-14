import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="312586",
    host="localhost",
    port=5432
)
cur = conn.cursor()

cur.execute("SELECT py_add(%s, %s);", (10, 20))
print(cur.fetchone()[0])  # 30

cur.close()
conn.close()
