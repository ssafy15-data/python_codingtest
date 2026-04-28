import sys; input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

# 정수 범위니까 투 포인터를 양쪽 끝에서부터 시작
for target in range(n):
    left, right = 0, n - 1
    while left < right:
        if arr[left] + arr[right] < arr[target]:
            left += 1
        elif arr[left] + arr[right] > arr[target]:
            right -= 1
        else:
            if left != target and right != target:
                count += 1
                break
            elif left == target:
                left += 1
            elif right == target:
                right -= 1

print(count)