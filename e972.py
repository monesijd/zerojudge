own_money = int(input())
buy_money, which_money = input().split()
buy_money = int(buy_money)
money_list = [["T", 1], ["U", 30.9], ["J", 0.28], ["E", 34.5]]
for i in range(4):
    if money_list[i][0] == which_money:
        own_money /= money_list[i][1]

last_money = own_money - buy_money
if last_money < 0:
    print("No Money")
elif 0 <= last_money <= 0.5:
    print(f"{which_money} 0.00")
else:
    print(f"{which_money} {last_money:.2f}")
