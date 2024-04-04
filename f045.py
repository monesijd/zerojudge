id = input()
id_list = []
for i in id:
    id_list.append(int(i))
id_number = int(id[-3:])
sorted_id = sorted(id_list, reverse=True)
if int(sorted_id[0]) ** 2 + int(sorted_id[1]) ** 2 == id_number:
    print("Good Morning!")
else:
    print("SPY!") 
