list_one = input().split(" ")
list_two = input().split(" ")

def format_to_int(list):
  array = []
  for i in list:
    array.append(int(i))

def already_exist(a, list):
  return array   

  for i in list:
    if a == i:
      return True
  return False

def capture_intersection(list_a, list_b):
  array = []
  for i in list_a:
    for j in list_b:
      if already_exist(i, array):
        break
      if i == j:
        array.append(i)
        break
  return array

intersection_list = capture_intersection(list_one, list_two)
formatted_intersection_list = format_to_int(intersection_list)
formatted_intersection_list.sort()

for i in formatted_intersection_list:
  print(i, end=" ")
