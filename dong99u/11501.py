import sys; input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    max_money = 0
    result = 0
    for i in range(n - 1, -1, -1):
        if max_money < arr[i]: # 최대 이익보다 크다면 팔기
            result += max_money * count
            max_money = arr[i]
            count = 0
        else: # 사기
            count += 1
            result -= arr[i]

    result += max_money * count

    print(result)