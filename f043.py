answer, first_number = map(int, input().split())
if answer == first_number:
    if answer - 3 < 3:
        print(f"{answer-3}+3={answer}")
    else:
        print(f"3+{answer-3}={answer}")
else:
    if answer - first_number < first_number:
        print(f"{answer-first_number}+{first_number}={answer}")
    else:
        print(f"{first_number}+{answer-first_number}={answer}")
