import json
import datetime


class Response:

    def __init__(self):
        self.request_id = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

    def generate_success(self):
        body = {
            'message': 'Success!'
        }
        headers = {
            'celiloda-request-id': self.request_id
        }
        return {
            'statusCode': 200,
            'headers': json.dumps(headers),
            'body': json.dumps(body)
        }

    def generate_fail(self, **kwargs):
        detail = kwargs.get('detail', default=None)
        body = {
            'message': 'Failed',
            'detail': detail
        }
        headers = {
            'celiloda-request-id': self.request_id
        }
        return {
            'statusCode': 500,
            'headers': json.dumps(headers),
            'body': json.dumps(body)
        }
