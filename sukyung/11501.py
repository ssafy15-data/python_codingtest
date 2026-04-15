# 주식 - Silver 2

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    price = arr[N-1]
    ans = 0
    # 맨 뒤에서 2번째 날의 주가부터 훑기 시작
    for i in range(N-2, -1, -1):
        # 전 날의 주가가 현재 주가보다 작다면 이익을 얻을 수 있으므로 계산
        if arr[i] < price:
            ans += price - arr[i]
        # 현재 주가보다 크다면 이익을 볼 수 없으므로 price를 새로 설정
        else:
            price = arr[i]
    print(ans)