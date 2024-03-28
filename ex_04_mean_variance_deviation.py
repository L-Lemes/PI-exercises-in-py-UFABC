x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())

def media(x1, x2, x3, x4):
  result = (x1 + x2 + x3 + x4) / 4
  return result

def variancia(x1, x2, x3, x4):
  m  = media(x1, x2, x3, x4)
  result = ((x1 - m)**2 + (x2 - m)**2 + (x3 - m)**2 + (x4 - m)**2) / 3 
  return result

def desvio(x1, x2, x3, x4):
  v =  variancia(x1, x2, x3, x4)
  result = v ** (1/2)
  return result

print("media = {:.2f}".format(media(x1, x2, x3, x4)))
print("variancia = {:.2f}".format(variancia(x1, x2, x3, x4)))
print("desvio = {:.2f}".format(desvio(x1, x2, x3, x4)))