
import json
import guten
from bottle import route, run, request, abort, default_app
from validate_email import validate_email
from models import TextSchedule
from schedule_handler import ScheduleHandler

text_schedule_handler = ScheduleHandler()

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

    text_schedule = TextSchedule.from_json(schedule_json)
    handle_new_schedule(text_schedule)

    return u''

@route('/schedules', method='GET')
def get_all_schedules():
    """ Returns a list of all scheduled readers """

    schedules = text_schedule_handler.get_schedule_list()
    schedule_strings = [str(schedule) for schedule in schedules]

    return schedule_strings

def validate_schedule_json(schedule_json):
    if not schedule_json.has_key(u'email'):
        abort(400, 'No email specified')

    if not validate_email(schedule_json[u'email']):
        abort(400, 'Email is invalid')

    if not schedule_json.has_key(u'gutenberg_id'):
        abort(400, 'No Gutenberg Book ID specified')

    if not schedule_json.has_key(u'days_to_read'):
        schedule_json[u'days_to_read'] = 30

def handle_new_schedule(text_schedule):
    # send first chunk right on sign up :)
    text_schedule_handler.send_next_chunk_for_schedule(text_schedule)

    # add schedule to redis
    text_schedule_handler.add_schedule(text_schedule)

# Run bottle internal test server when invoked directly ie: non-uxsgi mode
if __name__ == '__main__':
    run(host='localhost', port=8080)

# Run bottle in application mode. Required in order to get the application working with uWSGI!
else:
    app = application = default_app()
