number_input = input()
vote_box = [0 for i in range(11)]
k = 0
while k < len(number_input):
    vote_box[int(number_input[k])] += 1
    k += 1

sorted_box = sorted(vote_box, reverse=True)

for i in range(11):
    for j in range(11):
        if sorted_box[i] == vote_box[j] and sorted_box[i] != 0:
            vote_box[j] = 0
            print(f"{j} ", end="")
            break
