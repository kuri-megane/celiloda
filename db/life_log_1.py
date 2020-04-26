from db.connect import Connector
import datetime


class LifeLog1:

    def _get_time(self):
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    def insert(self, kind, val):
        self._get_time()
        with Connector() as connect:
            cursor = connect.cursor()
            cursor.execute(
                'INSERT INTO lifelog1 (kind, dt, val) VALUES (%s, %s, %s)',
                (kind, self.dt, val)
            )
            cursor.close()

    def check_records(self):
        with Connector() as connect:
            cursor = connect.cursor()
            cursor.execute(
                'SELECT * FROM lifelog1 ORDER BY id DESC limit 5'
            )
            rows = cursor.fetchall()
            result = [row for row in rows]
            cursor.close()
        return result

