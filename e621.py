height, weight, change_number = map(int, input().split())
change_number -= 1
seat_list = []
for i in range(height):
    seat_list.append([])
    for j in range(weight):
        seat_list[i].append(i*weight+j+1)

for _ in range(1, change_number+1):
    if _ % 2 == 1:
        for i in range(height):
            seat_list[i].insert(0, seat_list[i].pop())
          
    if _ % 2 == 0:
        seat_list.insert(0, seat_list.pop())


for i in range(height):
    for j in range(weight):
        print(seat_list[i][j], end=" ")
    print() 
