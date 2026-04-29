import sys; input = lambda: sys.stdin.readline().rstrip()

MAX_SIZE = 10 ** 7


def is_valid(mid):
    count = 0
    for i in range(n):
        for j in range(n):
            count += min(mid, grid[i][j])
    return count >= thresh_hold

def search():
    left, right = 0, MAX_SIZE
    result = MAX_SIZE

    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid - 1
            result = min(result, mid)
        else:
            left = mid + 1
    return result

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

total = sum(grid[i][j] for i in range(n) for j in range(n))
thresh_hold = total / 2

print(search())
