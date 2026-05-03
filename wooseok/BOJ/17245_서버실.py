import sys

data = sys.stdin.read().split()

grid = sorted(map(int, data[1:]))
n = len(grid)

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + grid[i]

total = prefix[n]
half = (total + 1) // 2

low = 0
high = grid[-1]
res = 0

while low <= high:
    mid = (low + high) >> 1

    l, r = 0, n
    while l < r:
        m = (l + r) >> 1
        if grid[m] < mid:
            l = m + 1
        else:
            r = m
    idx = l

    cur_sum = prefix[idx] + (n - idx) * mid
    
    if cur_sum >= half:
        res = mid
        high = mid - 1
    else:
        low = mid + 1

print(res)