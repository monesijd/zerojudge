width, height = map(int, input().split())
number = int(input())

my_map = []
for i in range(width):
    my_map.append(input().split())


my_str_number = 97
my_list = []
find_number = 0
for i in range(26):
    for j in range(width):
        for k in range(height):
            if my_map[j][k] == chr(my_str_number+i):
                my_list.append([j, k])
                find_number += 1

if find_number >= number:
    for i in range(number):
        print(my_list[i][0], my_list[i][1])
else:
    print("Mission fail.")
