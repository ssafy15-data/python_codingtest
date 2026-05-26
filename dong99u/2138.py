import sys; input = lambda: sys.stdin.readline().rstrip()

def click(arr, i):
    for j in range(3):
        if i + j <= n - 1:
            arr[i + j] ^= 1

n = int(input())
arr = list(map(int, list(input())))
target = list(map(int, list(input())))

answer = 1e9
arr1 = arr[:]

count = 0
for i in range(n - 1):
    if arr[i] != target[i]:
        count += 1
        click(arr, i)

if arr[-1] == target[-1]:
    answer = min(answer, count)

arr1[0] ^= 1
arr1[1] ^= 1
count = 1
for i in range(n - 1):
    if arr1[i] != target[i]:
        count += 1
        click(arr1, i)

if arr1[-1] == target[-1]:
    answer = min(answer, count)

print(answer if answer != 1e9 else -1)