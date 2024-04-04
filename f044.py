big_slime, little_slime = map(int, input().split())
end_number = (big_slime + little_slime) // big_slime
day = 1
while end_number != 1:
    end_number = end_number // 2
    day += 1
print(day-1) 
