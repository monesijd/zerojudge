height, weight= map(int, input().split())
drawing = [input().split() for i in range(height)]
# drawing[height][weight]
# 直排
for i in range(height):
    number = 0
    answer_height = -1
    first_index = 0
    last_index = 0
    for j in range(weight):
        if drawing[i][j] == "1" and number == 0:
            number += 1
            first_index = j
        elif drawing[i][j] == "1" and number == 1:
            last_index = j
            for _ in range(first_index, last_index+1):
                drawing[i][_] = 1
            number = 0

for i in range(height):
    for _ in range(weight):
        print(f"{drawing[i][_]} ", end="")
    print() 
