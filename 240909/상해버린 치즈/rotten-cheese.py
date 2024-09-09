n, m, d, s = map(int, input().split())
eat_record = [list(map(int, input().split())) for _ in range(d)]
sick_record = [list(map(int, input().split())) for _ in range(s)]


spoiled_cheese = []

for cheese in range(1, m + 1):

    cnt = 0
    temp = []

    for eat in eat_record:
        if eat[0] in temp:
            continue
        for sick in sick_record:
            if sick[0] == eat[0] and cheese == eat[1] and sick[1] > eat[2]:
                temp.append(eat[0])
                cnt += 1
    
    if cnt == s:
        spoiled_cheese.append(cheese)


res_person = set()

for eat in eat_record:
    if eat[1] in spoiled_cheese:
        res_person.add(eat[0])            

print(len(res_person))