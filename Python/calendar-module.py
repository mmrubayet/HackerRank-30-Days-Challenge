import calendar
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
# print(calendar.weekday(y, m, d))
# print(list(calendar.day_name)[5].upper())
# print(calendar.day_name[5])
