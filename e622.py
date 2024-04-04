pet_number, own_money = map(int, input().split())
Max_cp = 0
Max_index = None
for i in range(pet_number):
    cp, iv = map(int, input().split())
    sum_cp = cp
    levelup_number = own_money // 1000
    if iv <= 29:
        sum_cp += 10 * levelup_number
    elif 30 <= iv <= 39:
        sum_cp += 50 * levelup_number
    elif 40 <= iv <= 45:
        sum_cp += 100 * levelup_number
    if sum_cp > Max_cp:
        Max_cp = sum_cp
        Max_index = i

print(Max_index+1, Max_cp)
