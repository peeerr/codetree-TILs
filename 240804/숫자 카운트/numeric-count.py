n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ok, res = 0, 0

for i in range(1, 10):
    for j in range(i + 1, 10):
        for k in range(j + 1, 10):

            for x in arr:
                n1, n2, n3 = list(map(int, list(str(x[0]))))
                cnt1, cnt2 = x[1], x[2]
                tmp_cnt1, tmp_cnt2 = 0, 0
                
                if i == n1:
                    tmp_cnt1 += 1
                elif i in [n1, n2, n3]:
                    tmp_cnt2 += 1
                if j == n2:
                    tmp_cnt1 += 1
                elif j in [n1, n2, n3]:
                    tmp_cnt2 += 1
                if k == n3:
                    tmp_cnt1 += 1
                elif k in [n1, n2, n3]:
                    tmp_cnt2 += 1

                if tmp_cnt1 == cnt1 and tmp_cnt2 == cnt2:
                    ok += 1

            if ok == n:
                res += 1

print(res)