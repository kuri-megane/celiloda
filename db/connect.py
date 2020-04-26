import mysql.connector

from settings import *

config = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
    'database': DB_NAME,
}


class Connector(object):

    def __init__(self):
        self.config = config

    def __enter__(self):
        self.connect = mysql.connector.connect(
            db=self.config.get('database'),
            host=self.config.get('host'),
            user=self.config.get('user'),
            passwd=self.config.get('password'),
        )
        return self.connect

    def __exit__(self, exception_type, exception_value, traceback):
        self.connect.commit()
        self.connect.close()
