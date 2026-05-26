# 전구와 스위치 - Gold 4

def switch(i, b):
    if i-1 >= 0:  # i-1번째 전구가 존재하는 경우
        b[i-1] ^= 1
    b[i] ^= 1
    if i+1 < N:  # i+1번째 전구가 존재하는 경우
        b[i+1] ^= 1

N = int(input())
# input()에는 개행 문자 '\n'이 포함되므로 strip() 필요
before = list(map(int, input().strip()))
after = list(map(int, input().strip()))

if before == after:  # 전과 후의 상태가 동일한 경우
    ans = 0
else:
    '''
    i=1 부터는 i-1이 after와 다른 경우만 확인 후, switch 여부 결정하면 됨
    그러면, i=0인 경우의 수만 나눠서 비교하면 됨
    '''
    ans = int(1e9)  # 최댓값 설정 -> int형 사용할 것이므로 int() 선언
    # 1번 전구를 switch 하는 경우
    bulb = before.copy()
    switch(0, bulb)
    cnt = 1
    for i in range(1, N):
        # 항상 i-1번째 전구의 상태만 비교 후 switch 할지 말지 결정
        if bulb[i-1] != after[i-1]:
            switch(i, bulb)
            cnt += 1 
    if bulb == after: ans = cnt
    
    # 1번 전구를 switch 하지 않는 경우
    bulb = before.copy()
    cnt = 0
    for i in range(1, N):
        if bulb[i-1] != after[i-1]:
            switch(i, bulb)
            cnt += 1   
    if bulb == after: ans = min(ans, cnt)
    
    ans = -1 if ans == 1e9 else ans
    
print(ans)