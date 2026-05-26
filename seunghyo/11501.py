N = int(input())

for tc in range(N):
    day_n = int(input())
    days = list(map(int, input().split()))
    profit = 0
    max_price = days[-1]

    for idx in range(day_n - 2, -1, -1):
        if max_price > days[idx]:
            profit += max_price - days[idx]
        else:
            max_price = days[idx]
    print(profit)