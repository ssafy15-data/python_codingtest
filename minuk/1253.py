import sys;input=lambda:sys.stdin.readline().rstrip()

N = int(input())
ary = [*map(int, input().split())]

num_count = dict()
hm = dict()

zero_count = 0
for i in range(N):
    if (ary[i] == 0): zero_count += 1
    if (ary[i] not in num_count): num_count[ary[i]] = 0
    num_count[ary[i]] += 1
    hm[ary[i]] = 0

if (zero_count):
    for i in range(N):
        if (ary[i] == 0): continue
        if (num_count[ary[i]] >= 2): hm[ary[i]] = 1

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if (ary[i] == 0 or ary[j] == 0): continue
        if (ary[i] + ary[j] in hm):
            hm[ary[i] + ary[j]] = 1

if (zero_count >= 3): hm[0] = 1
for i in range(N):
    ans += hm[ary[i]]
print(ans)

# 원래는 투포인터로 탐색해서 찾는 건데, 귀찮아서 그냥 이중 for문으로 풀 수 없나 해서 풀었음
# 보니까 자기 자신이 아닌 서로 다른 두 수를 써서 자기 자신을 만들 수 있으면 된다 이므로
# 0에 대해서만 예외처리하면 이중 for문으로 풀 수 있음
# 결과적으로 0이 1개 이상일 경우, 각 숫자가 같은 숫자가 2개 이상이면 자기 자신을 만들 수 있음
# 0이 3개 이상일 경우 0도 좋은 수가 됨
# 이거에 대해 예외처리를 하고 hash map으로 만든 후, 배열을 다시 순회하면서 ans에 더해주면 됨