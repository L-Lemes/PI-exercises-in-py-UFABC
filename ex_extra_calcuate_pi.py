import sys

def pi(value):
  i = 1
  div = 1
  pi = 0
  
  while i <= value:
    if i % 2 == 1:
      pi += 1/div
    else:
      pi = pi - 1/div
    div += 2
    i += 1
  return pi
    
for line in sys.stdin:
  line = int(line)
  print(f'pi({line}) = {pi(line)*4:.4f}')

