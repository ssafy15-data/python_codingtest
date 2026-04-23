import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

n = int(input())
m = int(input())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr = list(map(int, input().split()))

parent = [i for i in range(n + 1)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i + 1, j + 1)

root = find(arr[0])  # 첫 번째 도시의 루트

flag = True
for city in arr:
    if find(city) != root:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')