import sys

input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

n = int(input())
a = [*map(int, input().split())]

a.sort()
res = 0
for i in range(n):
    left = 0
    right = n - 1

    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        
        if a[left] + a[right] == a[i]:
            res += 1
            break
        elif a[left] + a[right] < a[i]:
            left += 1
        elif a[left] + a[right] > a[i]:
            right -= 1

print(res)
