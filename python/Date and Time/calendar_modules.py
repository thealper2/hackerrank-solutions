import calendar

month, day, year = map(int, input().split())
weekday_num = calendar.weekday(year, month, day)
weekday_name = calendar.day_name[weekday_num]
print(weekday_name.upper())