student_number = int(input())
id_list = []
name_list = []
for _ in range(student_number):
    student_id, student_name = input().split()
    id_list.append(student_id[-1])
    name_list.append([student_name, student_id[-1],int(student_id[0])])
    #name_list[[Alber, S, 6]]

id_list = sorted(id_list)

for _ in range(student_number):
    if id_list.count(id_list[_]) == 1:
        for i in range(len(name_list)):
            if id_list[_] == name_list[i][1]:
                print(f"{name_list[i][1]}: {name_list[i][0]}")
    else:
        min = 1000
        min_name = None
        min_capital = None
        for j in range(len(name_list)):
            if id_list[_] == name_list[j][1]:
                if name_list[j][2] < min:
                    min = name_list[j][2]
                    min_name = name_list[j][0]
                    min_capital = name_list[j][1]
                    pop_index = j
        print(f"{min_capital}: {min_name}")
        name_list[pop_index][2] = 1000
