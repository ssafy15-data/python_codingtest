import sys;input=lambda:sys.stdin.readline().rstrip()

res = []
for _ in range(int(input())):
    N = int(input())
    l = list(map(int, input().split()))

    ans = 0
    max_value = l[-1]
    for i in range(N - 2, -1, -1):
        ans += max(0, max_value - l[i])
        max_value = max(max_value, l[i])
    res.append(str(ans))
print('\n'.join(res))