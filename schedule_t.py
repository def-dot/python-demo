import time
from datetime import datetime, timedelta
import random
import schedule


def gen_title():
    curr_time = datetime.now()
    remain_seconds = (curr_time.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1) - curr_time).seconds
    r = []
    for _ in range(count):
        random_datetime = curr_time + timedelta(seconds=random.randint(0, remain_seconds))
        r.append(random_datetime)
    return r


if __name__ == "__main__":
    schedule.every(1).minutes.do(gen_title)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
