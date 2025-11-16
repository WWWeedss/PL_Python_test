# file: function_declaration.py

import psycopg2

# 数据库连接参数
DB_PARAMS = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '312586',
    'host': 'localhost',
    'port': 5432
}

import os
# 获取当前文件所在目录的绝对路径
project_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ai_parse')

# PL/Python 函数声明 SQL
CREATE_FUNCTION_SQL = f"""
CREATE OR REPLACE FUNCTION py_add(a integer, b integer)
RETURNS integer
AS $$
import sys
sys.path.append(r'{project_dir}')  # Python 文件所在目录

from python_function_definition import add

return add(a, b)
$$ LANGUAGE plpython3u;
"""

def create_plpython_function():
    """
    在 PostgreSQL 中创建 PL/Python 函数
    """
    conn = psycopg2.connect(**DB_PARAMS)
    try:
        with conn.cursor() as cur:
            cur.execute(CREATE_FUNCTION_SQL)
            conn.commit()
        print("PL/Python 函数 py_add 已创建或更新。")
    finally:
        conn.close()

create_plpython_function()
