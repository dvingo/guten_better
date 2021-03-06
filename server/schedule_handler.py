
import math
import json
import redis
import guten
from models import TextSchedule
from guten_email import send_guten_email

class ScheduleHandler:
    def __init__(self, list_key='guten_schedule_list'):
        self.redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.list_key = list_key

    def add_schedule(self, text_schedule):
        self.redisClient.rpush(self.list_key, text_schedule.to_json())

    def get_schedule_list(self):
        start_index = 0
        stop_index = self.redisClient.llen(self.list_key)
        schedule_list = self.redisClient.lrange(self.list_key, start_index, stop_index)

        model_list = [TextSchedule.from_json(json.loads(schedule_json)) for schedule_json in schedule_list]
        return model_list

    def send_next_chunk_for_schedule(self, text_schedule):
        if text_schedule.is_finished():
            return

        text = guten.get_text(text_schedule.gutenberg_id)
        chunk_index = text_schedule.days_sent
        chunk_length = int(len(text) / text_schedule.days_to_read)

        chunk_to_send = guten.get_next_text_chunk(text, chunk_index, chunk_length)
        send_guten_email(text_schedule.email, text_schedule.days_sent, chunk_to_send)

        text_schedule.increment_days_sent()

    def send_next_chunks_for_all_schedules(self):
        number_of_schedules = self.redisClient.llen(self.list_key)

        for i in range(number_of_schedules):
            schedule_json = self.redisClient.lindex(self.list_key, i)
            schedule = TextSchedule.from_json(json.loads(schedule_json))

            self.send_next_chunk_for_schedule(schedule)

            updated_json = schedule.to_json()
            self.redisClient.lset(self.list_key, i, updated_json)

    def cleanup_finished_schedules(self):
        number_of_schedules = self.redisClient.llen(self.list_key)
        schedule_list = self.redisClient.lrange(self.list_key, 0, number_of_schedules)

        finished_items = []
        for schedule_json in schedule_list:
            schedule = TextSchedule.from_json(json.loads(schedule_json))
            if schedule.is_finished():
                finished_items.append(schedule_json)

        for finished in finished_items:
            self.redisClient.lrem(self.list_key, 0, finished)
