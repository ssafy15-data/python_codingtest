# 탑 - Gold 5

'''
n = int(input())
height = list(map(int, input().split()))
tower = [0] * n  # 레이저 신호 수신하는 탑 번호
sub = [0] * n   # 레이저 신호 수신하는 탑과의 높이 차이

for i in range(1, n):
    j = i-1
    while j >= 0:
        # j번째 탑 높이가 i번째 탑 높이보다 같거나 큰 경우
        if height[j] >= height[i]:
            tower[i] = j
            sub[i] = height[j] - height[i]
            break
        # j번째 탑의 레이저를 수신하는 탑 높이가 현재 i번째 탑 높이보다 같거나 큰 경우
        elif sub[j] + height[j] >= height[i]:
            tower[i] = tower[j]
            sub[i] = sub[j] + height[j] - height[i]
            break
        # 0번째 탑까지 검사 끝낸 경우
        if j == 0: break
        
        j = tower[j]

for i in range(n):
    if tower[i] != 0: tower[i] += 1
    print(tower[i], end=' ')
'''


n = int(input())
height = list(map(int, input().split()))
stack = []  # [탑 idx][탑 높이] 담은 스택 -> 항상 탑의 높이가 내림차순으로 정렬되어 있음
tower = [0] * n  # 레이저 신호 수신하는 탑 번호

for i in range(n):
    # 스택의 최상단 탑의 높이가 현재 탑 높이보다 낮다면 pop
    # -> 현재 탑 높이보다 낮다면 앞으로도 영원히 사용할 일 없기 때문
    while stack and stack[-1][1] < height[i]:
        stack.pop()
    if stack:  # 스택에 값이 남아있다면 -> 그 값이 현재 탑 레이저 신호 수신하는 탑임
        tower[i] = stack[-1][0] + 1  # 1-based index이므로 1 더해줌
    # 현재 탑 번호와 높이 스택에 삽입
    stack.append((i, height[i]))

print(*tower)