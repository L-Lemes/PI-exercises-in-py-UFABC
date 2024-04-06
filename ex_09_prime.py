start_end = input().split()

start, end = start_end
array = []

def get_prime_number(list, x):
  is_prime = True
  
  for i in range(2, x):
    if x % i == 0:
      is_prime = False
          
  if is_prime:
    list.append(x)

for j in range(int(start), int(end) + 1):
  get_prime_number(array, j)

print(array)
