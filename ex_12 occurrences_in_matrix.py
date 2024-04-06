dimensoes = input().split()

array = []
repetidos = []

for i in range(int(dimensoes[0])):
  a = input()
  b = a.split(" ")
  for j in b:  
    array.append(j)

for i in range(len(array)):
  for j in range(len(array)):
    if i < j and array[i] == array[j]:
      if array[i] not in repetidos:
        repetidos.append(array[i])

# print(len(repetidos))
