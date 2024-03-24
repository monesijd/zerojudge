question_number, each_score = list(map(int, input().split()))
right_answer = list(map(int, input().split()))
student_number = int(input())

for _ in range(student_number):
    student_answer = list(map(int, input().split()))
    score = 0
    for each_question in range(question_number):
        if student_answer[each_question] == right_answer[each_question]:
            score += each_score
    print(score, end="\n")
