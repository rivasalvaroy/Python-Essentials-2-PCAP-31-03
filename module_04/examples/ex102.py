import calendar

c = calendar.Calendar(2)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
# Resultado: 2 3 4 5 6 0 1

print()

c.setfirstweekday(0)
for weekday in c.iterweekdays():
    print(weekday, end=" ")
