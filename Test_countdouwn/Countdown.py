import datetime
import time

exam_date = datetime.datetime(2024, 3, 30, 10, 0, 0)

while datetime.datetime.now() < exam_date:
    remaining = exam_date - datetime.datetime.now().replace(microsecond=0)
    print(f'\r{remaining}', end='')
    time.sleep(1)
else:
    print('GOOD LUCK')
