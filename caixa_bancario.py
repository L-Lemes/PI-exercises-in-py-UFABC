value = float(input('digite o valor: '))
def cashMachine(value):
  cem = 0  
  cem += value // 100
  value %= 100
  cinquenta = 0
  cinquenta = value // 50
  value %= 50
  vinte = 0
  vinte = value // 20
  value %= 20
  dez = 0
  dez += value // 10
  value %= 10
  cinco = 0    
  cinco += value // 5
  value %= 5
  dois = 0
  dois = value // 2
  value %= 2
  um = 0    
  um = value // 1
  value %= 1
  return (f'''
Cédulas de R$ 100.00: {cem:.0f}
Cédulas de R$ 50.00: {cinquenta:.0f}
Cédulas de R$ 20.00: {vinte:.0f}
Cédulas de R$ 10.00: {dez:.0f}
Cédulas de R$ 5.00: {cinco:.0f}
Cédulas de R$ 2.00: {dois:.0f}
Cédulas de R$ 1.00: {um:.0f}
''')
cashMachine(value)
