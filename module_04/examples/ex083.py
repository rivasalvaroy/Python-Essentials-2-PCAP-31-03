from datetime import date

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

d = d1 - d2
print(d)  # Muestra: 366 days, 0:00:00.
print(d * 2)  # Muestra: 732 days, 0:00:00.
