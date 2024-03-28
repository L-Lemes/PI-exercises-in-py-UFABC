import math

def sum(a, b):
  result = a + b
  return result
    
def sub(a, b):
  result = a - b
  return result

def div(a, b):
  result = a / b
  return result

def mul(a, b):
  result = a * b
  return result
    
def exp(a, b):
  result = a ** b
  return result
    
def rad(a):
  result = a ** (1/2)
  return result
    
def log(a):
  result = math.log10(a)
  return result

string = str(input())
command = string.split(" ")

if len(command) == 2:
  command[1] = float(command[1])
  [op, a] = command
  
  if op == 'RAIZ':
    print(round(rad(a), 2))
  else:
    print(round(log(a), 2))
else:
  command[1] = float(command[1])
  command[2] = float(command[2])
  [op, a, b] = command
  
  if op == 'SUM':
    print(round(sum(a, b), 2))
  elif op == 'DIF':
    print(round(sub(a, b), 2))
  elif op == 'DIV':
    print(round(div(a, b), 2))
  elif op == 'MULT':
    print(round(mul(a, b), 2))
  else:
    print(round(exp(a, b), 2))
