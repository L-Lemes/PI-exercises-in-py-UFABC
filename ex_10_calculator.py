import math, sys

for line in sys.stdin:
  op_valida = True
  expressao = line.split(" ")
  operacao = expressao[0]
    
  if operacao == "SUM":
    res = float(expressao[1]) + float(expressao[2])
  elif operacao == "DIF":
    res = float(expressao[1]) - float(expressao[2])
  elif operacao == "MULT":
    res = float(expressao[1]) * float(expressao[2])
  elif operacao == "DIV":
    if float(expressao[2]) == 0:
      op_valida = False
    else:
      res = float(expressao[1]) / float(expressao[2])
  elif operacao == "POT":
    res = float(expressao[1]) ** float(expressao[2])
  elif operacao == "RAIZ":
    res = float(expressao[1]) ** (1/2)
  elif operacao == "LOG10":
    res = math.log10(float(expressao[1]))
  else:
    op_valida = False

  if (op_valida):
    print(f'{res:.2f}')
  else:
    print("Operacao Invalida")
        