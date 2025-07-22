import datetime
import os.path
import re


file_location = os.path.dirname(__file__)
homework_location = os.path.dirname(os.path.dirname(file_location))
homework_file_location = os.path.join(homework_location, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file(homework_file_location):
    with open(homework_file_location, encoding='utf-8') as homework_13:
        for i, line in enumerate(homework_13, start=1):
            line = line.strip()
            match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{5}", line)
            date_str = match.group()
            date_format = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

            if i == 1:
                print(date_format + datetime.timedelta(days=7))

            elif i == 2:
                day_of_week = date_format.strftime('%A')
                print(day_of_week)

            elif i == 3:
                day_another_hours = date_format.replace(hour=0, minute=0, second=0, microsecond=0)
                last_day = datetime.datetime.now() - day_another_hours
                print(last_day)


read_file(homework_file_location)
