weather_list = [list(map(float, input().split())) for i in range(7)]

Max_day_sum = 0
Max_day_index = None
for i in range(7):
    sum = 0
    for j in range(4):
        sum = sum + weather_list[i][j]
    if sum > Max_day_sum or Max_day_index == None:
        Max_day_sum = sum
        Max_day_index = i

Max_time_sum = 0
time_list = ["morning", "afternoon", "night", "early morning"]
Max_time_index = None
for i in range(4):
    sum = 0
    for j in range(7):
        sum = sum + weather_list[j][i]
    if sum > Max_time_sum or Max_time_index == None:
        Max_time_sum = sum
        Max_time_index = i

print(Max_day_index+1)
print(time_list[Max_time_index])
