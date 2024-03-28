value = float(input('digite o valor: '))

def cashMachine(value):
  cem = 0
  cinquenta = 0
  vinte = 0
  dez = 0
  cinco = 0
  dois = 0
  um = 0
  
  cem += value // 100
  value %= 100
  
  cinquenta = value // 50
  value %= 50
      
  vinte = value // 20
  value %= 20
      
  dez += value // 10
  value %= 10
      
  cinco += value // 5
  value %= 5
      
  dois = value // 2
  value %= 2
      
  um = value // 1
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
Cédulas de R$ 100.00: {data["cem"]:.0f}
Cédulas de R$ 50.00: {data["cinquenta"]:.0f}
Cédulas de R$ 20.00: {data["vinte"]:.0f}
Cédulas de R$ 10.00: {data["dez"]:.0f}
Cédulas de R$ 5.00: {data["cinco"]:.0f}
Cédulas de R$ 2.00: {data["dois"]:.0f}
Cédulas de R$ 1.00: {data["um"]:.0f}
''')

