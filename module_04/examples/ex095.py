import calendar

c = calendar.Calendar()

for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")

print("\n", "-"*50)

for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")

print("\n", "-"*50)

for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")
