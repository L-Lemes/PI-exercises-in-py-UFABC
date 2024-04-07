import sys

for line in sys.stdin:
  line = int(line)
  divisors = 0
  for i in range(1, line):
    if line % i == 0:
      print(i)
      divisors += i
  if divisors == line:
    print('Perfeito')
  else:
    print('Não Perfeito')
