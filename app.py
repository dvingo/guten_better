
import json
from guten import get_guten_text, get_next_text_chunk
from bottle import route, run, request, abort
from validate_email import validate_email

@route('/schedule', method='POST')
def post_new_book_schedule():
    """
    Post to this endpoint to add a new reader.

    Post data should be json with the following mandatory keys:
        'email': the email address to send daily reading chunks to
        'gutenberg_id': The ID for a given Project Gutenberg text

    Post data *can* include the following optional keys:
        'days_to_read': Number of days the reader would like to read text in; defualts to 30
    """

    data = request.body.readline()
    if not data:
        abort(400, 'No data received')

    schedule_json = json.loads(data)
    validate_schedule_json(schedule_json)

    return json.dumps(schedule_json)

def validate_schedule_json(schedule_json):
    if not schedule_json.has_key('email'):
        abort(400, 'No email specified')

    if not validate_email(schedule_json['email']):
        abort(400, 'Email is invalid')

    if not schedule_json.has_key('gutenberg_id'):
        abort(400, 'No Gutenberg Book ID specified')

    if not schedule_json.has_key('days_to_read'):
        schedule_json['days_to_read'] = 30

run(host='localhost', port=8080)
