date = input().split("/")

day = int(date[0])
month = int(date[1])
year = int(date[2])

months = [1, 3, 5, 7, 8, 10, 12]

def check_month(month):
  for i in months:
    if i == month:
      return True

if (check_month(month)):
  if day < 31:
    day += 1
  else:
    if (month == 12):
      day = 1
      month = 1
      year += 1
    else:
      day = 1
      month += 1
elif (month != 2):
  if day < 30:
    day += 1
  else:
    day = 1
    month += 1
else:
  if day < 28:
    day += 1
  else:
    day = 1
    month += 1

print(f'{day:02d}/{month:02d}/{year:02d}')    
