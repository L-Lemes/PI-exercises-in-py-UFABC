import math
entrada = str(input())
saida = str(input())

h_entrada = int(entrada.split(":")[0])
min_entrada = int(entrada.split(":")[1])

time_entrada = h_entrada * 60 + min_entrada

h_saida = int(saida.split(":")[0])
min_saida = int(saida.split(":")[1])

time_saida = h_saida * 60 + min_saida

time_total = time_saida - time_entrada

contador = float(0)

if time_total <= 15:
  print(f'R$ {contador:.2f}')
elif time_total > 15 and time_total <= 60:
  contador += 5
  print(f'R$ {contador:.2f}')
elif time_total > 60 and time_total <= 240:
  value = time_total / 60
  value = math.ceil(value)
  value -=1
  value *=3
  contador += value + 5
  print(f'R$ {contador:.2f}')
elif time_total > 240:
  value = time_total / 60
  value = math.ceil(value)
  value -= 4
  value *= 2
  contador += value + 14
  print(f'R$ {contador:.2f}')
