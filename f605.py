number, d = map(int, input().split())
buy_number = 0
buy_money = 0

for _ in range(number):
    price = list(map(int, input().split()))
    average = int((price[0] + price[1] + price[2]) / 3)
    sorted_price = sorted(price)
    if sorted_price[2] - sorted_price[0] >= d:
        buy_number += 1
        buy_money += average


print(buy_number, buy_money) 
