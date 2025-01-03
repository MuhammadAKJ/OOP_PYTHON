lists = [1, 2, 3, 4, 5, 6]

reversed_list = []

for i in range(len(lists)):
    reversed_list.append(lists[-i-1])

print(reversed_list)