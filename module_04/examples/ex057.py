from datetime import date

d = date(2019, 11, 4)
print(d.weekday())      # 0(Monday) - 6(Sunday)
print(d.isoweekday())   # 1(Monday) - 7(Sunday)
