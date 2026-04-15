import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())  # N: 카드 개수, M: 게임 진행 횟수
do, su = deque(), deque()
for _ in range(N):
    d, s = map(int, input().split())
    # 맨 아래에 위치한 카드 -> 맨 위에 위치한 카드 순서
    do.append(d)
    su.append(s)

'''
도도 -> 수연 순서
가장 위에 위치한 카드 내려놓음
수연: 카드의 숫자 합 = 5, 어느 쪽의 그라운드도 비어있으면 X
도도: 카드의 숫자가 5가 나오는 순간
종 치면 -> 상대방 카드 뒤집고 + 내 카드 뒤집어 합침
각각의 카드는 1<= <=5 자연수 적혀 있음
-> 즉, 도도와 수연 둘 다 종을 칠 수 있는 경우는 없음

게임 승패 결정 우선순의
1. 종 치기 전 덱 비어 있는지 확인
2. M번 진행 후 결과 비교
'''
winner = 'dosu'
d, s = deque(), deque()
for i in range(M):
    # 카드 제출
    if not i%2:    # 도도 차례인 경우
        d.append(do.pop())
        if not do:    # 카드 제출 후 덱 비어 있는지 확인
            winner = 'su'   # 비어 있다면 상대방 승리
            break                
    else:    # 수연 차례인 경우
        s.append(su.pop())
        if not su:
            winner = 'do'
            break
    
    # 종 치기
    # 각각의 카드 더미 중 위에 위치한 숫자가 5인 경우 -> 도도 종 치기
    if (d and d[-1]==5) or (s and s[-1]==5):
        do.extendleft(s)
        do.extendleft(d)
        s.clear()
        d.clear()
    # 둘 다 카드 제출 되어 있으면서 합이 5인 경우 -> 수연 종 치기
    elif d and s and d[-1]+s[-1] == 5:
        su.extendleft(d)
        su.extendleft(s)
        d.clear()
        s.clear()
        
if winner == 'dosu':  # 아직 승패가 안 난 경우
    if len(do) > len(su):
        winner = 'do'
    elif len(do) < len(su):
        winner = 'su'

print(winner)