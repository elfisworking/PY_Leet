import re


n, m = list(map(int, input().split()))
repair = list(map(int, input().split()))
stat = list(map(int, input().split()))
ans = 0
repair.sort()
stat.sort()
right = 0
for i in range(n):
    if right >= m:
        ans = 0
        break
    print(repair[i], stat[right])
    while right < m and repair[i] > stat[right]:
        right += 1
    if right == m:
        ans = 0
        break
    ans += stat[right]
if ans == 0:
    print(-1)
else:
    print(ans)
