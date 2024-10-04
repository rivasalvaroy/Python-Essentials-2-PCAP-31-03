import calendar

c = calendar.Calendar()

for data in c.monthdays2calendar(2024, 9):
    print(data)
