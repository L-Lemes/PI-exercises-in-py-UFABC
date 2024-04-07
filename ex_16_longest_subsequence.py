length = int(input())

arr = [] 

for i in range(length):
  arr.append(int(input())) #Armazeno os valores digitados em um array

matrix = []
for i in range (length):
  matrix.append([]) #Crio um matriz para receber cada subsequencia possivel

a = 0
for i in range(1, len(arr)): #Armazeno cada subsequencia na matriz criada
  if arr[i] > arr[i - 1]:
    if arr[i - 1] not in matrix[a]:
      matrix[a].append(arr[i - 1])
    if arr[i] not in matrix[a]:
      matrix[a].append(arr[i])
  else:
    a += 1
  
for i in range(0, len(matrix)):
  matrix[i] = len(matrix[i]) #Substituo cada subsequencia por seu comprimento
  if matrix[i] == 0:
    matrix[i] += 1

matrix.sort() # Ordeno seu comprimento

print(matrix[-1]) # Mostro o ultimo valor que é o maior
