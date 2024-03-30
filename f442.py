num = int(input())
chicken = list(map(int, input().split()))
eagle = int(input())
catch_num = int(input())
caught_chi = list(map(int, input().split()))

for each_chi in caught_chi:
    caught_index = chicken.index(each_chi)
    chicken[caught_index], eagle = eagle, chicken[caught_index]

for _ in chicken:
    print(_, end=" ")
