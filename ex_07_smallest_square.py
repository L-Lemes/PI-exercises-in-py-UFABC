value = int(input())

def menor_quadrado(value):
  for i in range(1, 100000):
    if i*i > value:
      return i

print(menor_quadrado(value))
