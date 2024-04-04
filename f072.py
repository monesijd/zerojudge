number = int(input())
ground = input().split()

one_number = 0
first_one = 1
last_one = 0
for j in range(number):
    if ground[j] == "1" and one_number == 0:
        first_one = j
        one_number += 1
    if ground[j] == "1":
        last_one = j
for j in range(first_one):
    ground.pop(0)
for j in range(number-last_one-1):
    ground.pop(-1)

for i in range(1, len(ground)-1):
    if ground[i] == "9":
        if ground[i+1] != "9":
            ground[i+1] = 1
        if ground[i-1] != "9":
            ground[i-1] = 1

print(ground.count("0"))
