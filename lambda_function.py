import mysql.connector
import os

from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

env_file_path = join(dirname(__file__), '.env')
load_dotenv(env_file_path)


DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]


def execute_query(event):
    config = {
        'user': DB_USER,
        'password': DB_PASSWORD,
        'host': DB_HOST,
        'database': DB_NAME,
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    kind = 2
    dt = '2020-04-19 20:26:46.010111'
    val = 37.2

    # insert
    ret = cursor.execute('insert into lifelog1 (kind, dt, val) values (%s, %s, %s)', (kind, dt, val))
    print(ret)

    # # select
    # cursor.execute('select * from lifelog1')
    # row = cursor.fetchone()
    #
    # # 出力
    # for i in row:
    #     print(i)

    # データベースから切断
    cursor.close()
    cnx.commit()
    cnx.close()


def lambda_handler(event, context):
    execute_query(event)
