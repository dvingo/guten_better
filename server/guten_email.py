import os
import boto.ses

with open('./stuff.txt') as f:
    lines = f.read().splitlines()
    AWS_ACCESS_KEY_ID = lines[0]
    AWS_SECRET_ACCESS_KEY = lines[1]

def send_guten_email(recipient, day, chunk):
    subject = u'Page a day club, Day {}'.format(day)
    body = chunk
    send_email(recipient, subject, body)

def send_email(recipient, subject, body):
    conn = boto.ses.connect_to_region(
        'us-east-1',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    conn.send_email('read@pageaday.club', subject, body, [recipient])
