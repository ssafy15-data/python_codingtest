from sys import stdin
import heapq

n, l = map(int, stdin.readline().split())
ary = map(int, stdin.readline().split())
min_heap = []
res = [0 for i in range(n)]
i = 0
for data in ary:
	m = i - l
	while (len(min_heap) != 0 and min_heap[0][1] <= m):
		heapq.heappop(min_heap)
	heapq.heappush(min_heap, (data, i))
	res[i] = min_heap[0][0]
	i += 1
print(*res)