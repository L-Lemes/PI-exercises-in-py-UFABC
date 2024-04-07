prime = []
not_prime = []

num = int(input())

while num != -1:
  is_prime = True
  for i in range(2, num):
    if num % i == 0:
      is_prime = False
  
  if is_prime == True:
    prime.append(num)
  else:
    not_prime.append(num)

  num = int(input())

print(*not_prime)
print(*prime)
