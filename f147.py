import numbers

combo = [0, "Medium Wac", "WChicken Nugget", "Geez Burger", "ButtMilk Crispy Chicken", "Plastic Toy"]
combo_price = [0, 4, 8, 7, 6, 3]
single = [0, "German Fries", "Durian Slices", "WcFurry", "Chocolate Sunday"]
single_price = [0, 2, 3, 5, 7]
total = 0
while True:
    number = int(input())
    if number == 0:
        print(f"Total: {total}")
        break
    food_number = int(input())
    if number == 1:
        print(f"{combo[food_number]} {combo_price[food_number]}")
        total += combo_price[food_number]
    if number == 2:
        print(f"{single[food_number]} {single_price[food_number]}")
        total += single_price[food_number]
