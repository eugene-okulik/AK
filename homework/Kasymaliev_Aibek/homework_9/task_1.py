import datetime


request_date = 'Jan 15, 2023 - 12:05:33'

response_date = datetime.datetime.strptime(request_date, '%b %d, %Y - %H:%M:%S')

print(response_date.strftime('%B'))
print(response_date.strftime('%d.%m.%y, %H:%M'))
