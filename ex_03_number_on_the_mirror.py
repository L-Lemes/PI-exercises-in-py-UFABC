value = int(input())

def reverse_numbers(value):
  reversed = ""
  while value > 0:
    reversed += str(value % 10)
    value //= 10
  
  return int(reversed)
    
print(reverse_numbers(value))