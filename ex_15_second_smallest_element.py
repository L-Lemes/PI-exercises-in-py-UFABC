import sys

def capture_inputs():
    array = []
    for line in sys.stdin:
        array.append(int(line))
    array.pop(0)
    return array

def sort_list(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

array = capture_inputs()
sorted_list = sort_list(array)

print(sorted_list[1])
