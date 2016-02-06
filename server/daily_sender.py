
from schedule_handler import ScheduleHandler

def main():
    text_schedule_handler = ScheduleHandler()
    text_schedule_handler.send_next_chunks_for_all_schedules()

    text_schedule_handler.cleanup_finished_schedules()

if __name__ == '__main__':
    main()
