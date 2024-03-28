deslocamento = int(input())
mensagem = input()

mensagem_cifrada = ''

for i in range(len(mensagem)):
  if mensagem[i] == " ":
    mensagem_cifrada = mensagem_cifrada + mensagem[i]
  else:
    a = (ord(mensagem[i]) - 97 + deslocamento)%26 + 97
    mensagem_cifrada = mensagem_cifrada + chr(a)

print(mensagem)
print(mensagem_cifrada)

  