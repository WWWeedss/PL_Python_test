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
PROJECT_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')

# PL/Python 函数声明 SQL
CREATE_FUNCTION_SQL = f"""
CREATE OR REPLACE FUNCTION py_parse_document(path text, options text DEFAULT '{{}}', apikey text DEFAULT '')
RETURNS text
AS $$
import sys, json

root = r'{PROJECT_ROOT}'
if root not in sys.path:
    sys.path.append(root)

from src.ai_parse.python_function_definition import parse_document 
from src.ai_parse.utils.common_utils import str_to_dict

opts = str_to_dict(options)
result_str = parse_document(path, opts, apikey)

return result_str
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

if __name__ == "__main__":
    create_plpython_function()
