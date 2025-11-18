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

def process_articles():
    apikey = os.getenv("ZHIPUAI_API_KEY")
    if not apikey:
        raise RuntimeError("缺少环境变量 ZHIPUAI_API_KEY")

    sql = """
    INSERT INTO article_content (article_id, content)
    SELECT a.id,
           py_parse_document(
               a.article_url,
               '{"use_ai_correction": true, "model": "glm-4.5-flash"}',
               %s
           )::jsonb
    FROM articles a
    ORDER BY a.id;
    """
    cur.execute(sql, (apikey,))
    conn.commit()

if __name__ == "__main__":
    try:
        process_articles()
        print("文章内容处理完成。")
    finally:
        cur.close()
        conn.close()