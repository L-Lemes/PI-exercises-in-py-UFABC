start_end = input()

start = int(start_end.split(" ")[0])
end = int(start_end.split(" ")[1])
array = []

def get_prime_number(list, x):
  cont = 0
  
  for i in range(2, x):
    if x % i == 0:
      cont +=1
          
  if cont == 0:
    list.append(x)

for j in range(start, end + 1):
  get_prime_number(array, j)

print(array)