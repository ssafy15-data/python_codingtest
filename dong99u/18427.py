import sys; input = lambda: sys.stdin.readline().rstrip()

def backtrack(i, acc):
    '''
    start_idx 번째 학생의 블록을 고려할 때,
    acc만큼 탑의 높이를 쌓았다면
    '''
    if memo[i][acc] != -1:
        return memo[i][acc]

    if i == n:
        if acc == h:
            return 1
        else:
            return 0

    result = 0
    for j in range(len(arr[i])):
        if acc + arr[i][j] <= h:
            result += backtrack(i + 1, acc + arr[i][j])
    memo[i][acc] = result % 10007
    return memo[i][acc]


n, m, h = map(int, input().split())

# 효율적인 백트래킹을 위해 미리 정렬해서 받아옴
arr = [[0] + list(sorted(map(int, input().split()))) for _ in range(n)]

memo = [[-1] * (h + 1) for _ in range(n + 1)]

answer = backtrack(0, 0)
print(answer)