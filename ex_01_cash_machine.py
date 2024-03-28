value = float(input('digite o valor: '))

def cashMachine(value):
  cem = int(value // 100)
  value %= 100
  
  cinquenta = int(value // 50)
  value %= 50
  
  vinte = int(value // 20)
  value %= 20

  dez = int(value // 10)
  value %= 10
  
  cinco = int(value // 5)
  value %= 5
  
  dois = int(value // 2)
  value %= 2
  
  um = int(value // 1)
  value %= 1

  return {
    "cem": cem, 
    "cinquenta": cinquenta,
    "vinte": vinte,
    "dez": dez,
    "cinco": cinco,
    "dois": dois,
    "um": um
  }

data = cashMachine(value)

print(f'''
Cédulas de R$ 100.00: {data["cem"]}
Cédulas de R$ 50.00: {data["cinquenta"]}
Cédulas de R$ 20.00: {data["vinte"]}
Cédulas de R$ 10.00: {data["dez"]}
Cédulas de R$ 5.00: {data["cinco"]}
Cédulas de R$ 2.00: {data["dois"]}
Cédulas de R$ 1.00: {data["um"]}
''')

