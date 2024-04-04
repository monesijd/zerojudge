height, length = map(int, input().split())
teacher_map =  [input().split() for i in range(height)]
input()
elder_map = [input().split() for i in range(height)]

my_dict = {"length": [], "height": []}
#teacher_map[height][length]
for i in range(height):
    sum = 0
    for j in range(length):
        sum += int(elder_map[i][j])
    my_dict["length"].append(sum)

for i in range(length):
    sum = 0
    for j in range(height):
        sum += int(elder_map[j][i])
    my_dict["height"].append(sum)



for i in range(height):
    for j in range(length):
        if (my_dict["length"][i] + my_dict["height"][j] - int(elder_map[i][j])) % 2 == 1:
            if teacher_map[i][j] == '0':
                teacher_map[i][j] = '1'
            else:
                teacher_map[i][j] = '0'

for i in range(height):
    for j in range(length):
        print(teacher_map[i][j], end=" ")
    print()
