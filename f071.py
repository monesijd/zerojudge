lucky_number1, lucky_number2, bad_number = input().split()
first_list = input().split()
second_list = input().split()
money = 0

if lucky_number1 in first_list:
    for i in range(len(first_list)):
        if first_list[i] == lucky_number1:
            money += int(second_list[i])
if lucky_number2 in first_list:
    for i in range(len(first_list)):
        if first_list[i] == lucky_number2:
            money += int(second_list[i])
if bad_number in first_list:
    for i in range(len(first_list)):
        if first_list[i] == bad_number:
            money -= int(second_list[i])
else:
    money = money * 2

if money > 0:
    print(money)
else:
    print(0)
