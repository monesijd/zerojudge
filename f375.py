height, ask_height, patience = list(map(int, input().split()))
day = 1
    
while patience > 0:
    if day % 10 == 0:
        day += 1
        continue
    elif day % 10 == 1 and day != 1:
        if height < ask_height:
            patience -= 1
        if patience == 0:
            break
    else:
        if day % 3 == 1 and day != 1:
            height = height + (height//3)
        elif day != 1:
            height = height + (height//10)      
    if height >= ask_height:
        break
    day += 1

if patience == 0:
    print("unsalable")
else:
    print(day)
