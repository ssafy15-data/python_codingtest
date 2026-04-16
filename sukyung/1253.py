# 좋다 - Gold 4

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 투포인터 사용
arr.sort()
ans = 0
for k in range(N-1, -1, -1):
    num = arr[k]
    # 다른 수 2개의 합이 num이 되는 경우 탐색
    i, j = 0, N-1   # 같은 값이 여러 개 있는 경우도 있으므로, j값을 N-1로 초기화해 줌
    while i < j:
        # 서로 다른 수끼리 합해서 비교해야 함
        if i == k:
            i += 1
            continue
        if j == k:
            j -= 1
            continue

        if arr[i] + arr[j] == num:
            ans += 1
            print(num, k)
            break
        # arr이 정렬된 상태이므로 num보다 큰지 작은지에 따라 i, j 값 옮겨주면 됨
        elif arr[i] + arr[j] < num:
            i += 1
        elif arr[i] + arr[j] > num:
            j -= 1

print("ans:", ans)