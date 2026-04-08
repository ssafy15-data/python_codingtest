import heapq
n = int(input())
tops = list(map(int, input().split()))

pq = [(0, -tops[0])] # 위치, 높이
heapq.heapify(pq)
cur_max = tops[0] # 현재까지의 최대 높이, 양수로 저장
results = [0] # 수신받은 탑, 0 = 없음

for i in range(1, n):
    cur_top = tops[i] # 양수로 받음
    if cur_top > cur_max: # 양수로 비교
        pq = [(-i, -cur_top)] # 음수로 저장
        heapq.heapify(pq)
        results.append(0)
        cur_max = cur_top # 양수로 저장
    else:
        while True:
            prev_pos, prev_top = heapq.heappop(pq) # 음수로 받음
            prev_pos, prev_top = -prev_pos, -prev_top # 양수로 바꿈
            if prev_top >= cur_top: # 양수로 비교
                if prev_top > cur_top: # 양수로 비교
                    heapq.heappush(pq, (-prev_pos, -prev_top)) # 음수로 저장
                    heapq.heappush(pq, (-i, -cur_top)) # 음수로 저장
                results.append(prev_pos+1) # 양수로 저장
                break

print(" ".join(list(map(str, results))))