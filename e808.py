bus_stop_number = int(input())
hour, minute = map(int, input().split())

gap_list = []
for _ in range(bus_stop_number):
    gap_list.append(int(input().strip()))

time_list = [0]
for i in range(bus_stop_number):
    minute += gap_list[i]
    if minute >= 60:
        hour += (minute // 60)
        minute = minute % 60
        if hour >= 24:
            hour = hour % 24
    time_list.append([f"{hour:02d}", f"{minute:02d}"])

input_list = map(int, input().split())
for each_input in input_list:    
    if each_input == 0:
        break
    else:
        print(f"{time_list[each_input][0]}:{time_list[each_input][1]}")
