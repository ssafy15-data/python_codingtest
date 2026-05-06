import sys

input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

"""
1. 전구를 누르는 순서는 상관없음
  -> 앞에서부터 순서대로 누른다면 앞에서 부터 전구의 상태를 고정시킬 수 있음
  -> index i기준 i-1만 신경쓰자
2. 1번 또는 N번 위치를 누를 때만 특이 케이스 존재
  -> 누르는 순서는 상관없고 둘 중 하나는 다른 하나에 종속됨
  -> 첫 번째 전구를 누르는 경우와 누르지 않는 경우로 구분
=> 그리디
"""

# main code
n = int(input())
a = [*map(int, input())]
b = [*map(int, input())]

if a == b:
    print(0)
    sys.exit()

def flip(state, i):
    for j in range(i - 1, i + 2):
        if 0 <= j < n:
            state[j] ^= 1

def run(first):
    state = a[:]
    cnt = 0
    
    if first:
        flip(state, 0)
        cnt += 1
    
    for i in range(1, n):
        if state[i - 1] != b[i - 1]:
            flip(state, i)
            cnt += 1
    
    if state == b:
        return cnt
    else:
        return INF

res1 = run(True)
res2 = run(False)

res = min(res1, res2)
print(res if res != INF else -1)
