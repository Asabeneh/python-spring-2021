# there are quite  a lot of modules

from datetime import datetime, date, time
now = datetime.now()
day = now.day
# date = now.date()
month = now.month
year = now.year
hours = now.hour
minutes = now.minute
# print('date: ', date)
print(day)
print(month)
print(year)
print(f'{day}/{month}/{year} {hours}:{minutes}')
print(f'{day}-{month}-{year} {hours}:{minutes}')

timestamp = now.timestamp()
print(timestamp) # 1970 Janury 1, 00:00

# print(dir(datetime))


new_year = datetime(1970, 1, 1,2,30,40)
print(new_year)
print(new_year.day)
print(new_year.year)
print(new_year.hour)

print(now.strftime('%a %Y/%m/%d %I:%M:%S %p'))
print(now.strftime('%A %d-%m-%Y %H:%M:%S'))
print(now.strftime('%d/%m/%Y %H:%M:%S'))
print(now.strftime('%c'))

date_string = "5 December, 2019"

print('WHAT IS IN HERE?', datetime.strptime(date_string, '%d %B, %Y'))

date_obj = datetime.strptime(date_string, '%d %B, %Y')

print(date_obj.day)
print(date_obj.year)
print(date_obj.month)
print(date_obj.hour)

d = date(2020, 1, 1)
print(d)
print(d.year, d.month, d.day)

t = time(10, 30, 15)
print(t)

today = date(now.year, now.month, now.day)
new_year = date(year=2022, month=1, day=1)
print('lets see', new_year - today)
print(d)
