
from json import dumps as json_dumps

class TextSchedule:

    def __init__(self, email, gutenberg_id, days_to_read=30, days_sent=0):
        self.email = email
        self.gutenberg_id = gutenberg_id
        self.days_to_read = days_to_read
        self.days_sent = days_sent

    def __str__(self):
        return self.to_json()

    def is_finished(self):
        return self.days_sent >= self.days_to_read

    def increment_days_sent(self):
        if self.is_finished():
            return

        self.days_sent += 1

    def to_json(self):
        return json_dumps({'email': self.email,
                           'gutenberg_id': self.gutenberg_id,
                           'days_to_read': self.days_to_read,
                           'days_sent': self.days_sent})

    @staticmethod
    def from_json(json):
        return TextSchedule(email=json[u'email'],
                            gutenberg_id=json[u'gutenberg_id'],
                            days_to_read=json[u'days_to_read'],
                            days_sent=json[u'days_sent'] if json.has_key(u'days_sent') else 0)
