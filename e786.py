input_string = input()
length = len(input_string)
if length % 2 == 0:
    number = 0
    for i in range(length//2):
        if input_string[i] == input_string[length-i-1]:
            number += 1
        else:
            break
    if number == (length // 2):
        print("YES")
        for _ in range(length//2):
            print(input_string[_], end="")
    else:
        print("NO")
else:
    print("NO")
