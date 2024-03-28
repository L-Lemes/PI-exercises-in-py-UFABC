import math

entry = str(input()).split(":")
exit = str(input()).split(":")

[h_entry, min_entry] = entry
time_entry = int(h_entry) * 60 + int(min_entry)

[h_exit, min_exit] = exit
time_exit = int(h_exit) * 60 + int(min_exit)

time_total = time_exit - time_entry

if time_total <= 15:
  print(f'R$ {0:.2f}')
elif time_total > 15 and time_total <= 60:
  print(f'R$ {5:.2f}')
elif time_total > 60 and time_total <= 240:
  value = math.ceil(time_total / 60)
  value = (value - 1) * 3 + 5
  print(f'R$ {value:.2f}')
elif time_total > 240:
  value = math.ceil(time_total / 60)
  value = (value - 4) * 2 + 14
  print(f'R$ {value:.2f}')
  