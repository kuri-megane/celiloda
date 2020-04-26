import json


class Request:

    def __init__(self, event, context):
        """
        :param event:
        :type event: dict
        :param context:
        :type context: dict
        """
        self.event = event
        self.context = context

    def _get_body(self):
        if 'body' in self.event:
            self.body = json.loads(self.event['body'])
        else:
            raise KeyError('cannot find body')

    def _get_val(self):

        if 'kind' in self.body:
            self.kind = self.body['kind']
        else:
            raise KeyError('cannot find kind')

        if 'val' in self.body:
            self.val = self.body['val']
        else:
            raise KeyError('cannot find val')

    def get(self):
        self._get_body()
        self._get_val()
        return self.kind, self.val
