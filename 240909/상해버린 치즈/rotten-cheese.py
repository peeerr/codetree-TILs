n, m, d, s = map(int, input().split())
eat_record = [list(map(int, input().split())) for _ in range(d)]
sick_record = [list(map(int, input().split())) for _ in range(s)]


spoiled_cheese = set()

for cheese in range(1, m + 1):

    cnt = 0

    for sick in sick_record:
        sick_person, sick_time = sick[0], sick[1]

        for eat in eat_record:
            if sick_person == eat[0] and cheese == eat[1] and sick_time > eat[2]:
                cnt += 1
    
    if cnt == s:
        spoiled_cheese.add(cheese)


res_person = set()

for eat in eat_record:
    if eat[1] in spoiled_cheese:
        res_person.add(eat[0])            

print(len(res_person))