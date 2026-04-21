import sys

input = lambda: sys.stdin.readline().rstrip()

# main code
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if rank[a] > rank[b]:
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[b] = a
            rank[a] += 1

n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

for i in range(n):
    query = [*map(int, input().split())]
    for j, v in enumerate(query):
        if v:
            union(i + 1, j + 1)

plan = [*map(int, input().split())]
root = find(plan[0])

for i in range(m):
    if root != find(plan[i]):
        print('NO')
        break
else:
    print('YES')
