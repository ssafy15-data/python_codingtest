import sys

input = lambda: sys.stdin.readline().rstrip()

# main code

"""
최대이익: 최대 cost에서 판매
어떠한 시점에서 구매는 최대 1회만 가능
역순으로 최댓값 탐색

-> max_price - prices[i]로 차익 계산
"""
T = int(input())
for tc in range(T):
    n = int(input())
    prices = [*map(int, input().split())]
    
    res = 0
    max_price = 0
    
    for i in range(n - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            res += max_price - prices[i]
        
    print(res)
