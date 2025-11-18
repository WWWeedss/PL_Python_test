import os

import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="312586",
    host="localhost",
    port=5432
)
cur = conn.cursor()

if __name__ == "__main__":
    apikey = os.getenv("ZHIPUAI_API_KEY")
    cur.execute("SELECT py_parse_document(%s, %s, %s);", (
        "https://plpython.oss-cn-beijing.aliyuncs.com/test.pdf",
        '{"use_ai_correction": true,'
        ' "model": "glm-4.5-flash"}',
        apikey
    ))
    print(cur.fetchone())  # 30

    cur.close()
    conn.close()