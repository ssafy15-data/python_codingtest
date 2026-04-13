import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    prices = list(map(int, input().split()))

    cum_prices = [0]
    for price in prices:
        cum_prices.append(cum_prices[-1]+price)
    
    prices = [(price, idx) for idx, price in enumerate(prices)]
    prices.sort(reverse=True)
    
    profit = 0
    cur_pos = 0
    for max_price, idx in prices:
        if idx == cur_pos:
            cur_pos += 1
            continue
        elif idx < cur_pos:
            continue
        else:
            profit += (idx - cur_pos) * max_price - (cum_prices[idx] - cum_prices[cur_pos])
            cur_pos = idx + 1
            if idx == n-1:
                break
    
    print(profit)