import sys
input = sys.stdin.readline

n = int(input())

coms = []
max_floor = 0
min_floor = 1
total = 0
for _ in range(n):
    line = list(map(int, input().split()))
    total += sum(line)
    max_floor = max(max_floor, max(line))
    coms.append(line)
half = total // 2 + total % 2

def cnt_coms(floor):
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += min(floor, coms[i][j])
    return cnt

floor = 0

while True:
    if max_floor == min_floor:
        floor = min_floor
        break
    elif max_floor - min_floor == 1:
        if cnt_coms(min_floor) >= half:
            floor = min_floor
            break
        else:
            floor = max_floor
            break

    middle = (min_floor + max_floor) // 2
    cnt = cnt_coms(middle)
    if cnt == half:
        floor = middle
        break
    elif cnt > half:
        max_floor = middle
    else:
        min_floor = middle

print(floor)
