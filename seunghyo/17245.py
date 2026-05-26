import sys


def solve():
    input = sys.stdin.readline
    N = int(input())

    servers = []
    server_sum = 0
    max_time = 0

    for _ in range(N):
        row = list(map(int, input().split()))
        servers.extend(row)
        server_sum += sum(row)
        max_time = max(max_time, max(row))

    # 예외 처리: 서버가 단 한 대도 없는 경우 바로 0 출력 후 종료
    if server_sum == 0:
        print(0)
        return

    # 절반(올림) 계산 - 실수 오차를 방지하기 위해 정수 연산(//) 활용
    limit_server = (server_sum + 1) // 2

    # --- 이분 탐색(Binary Search) 시작 ---
    low = 0
    high = max_time
    answer = 0

    while low <= high:
        # 중간 시간(mid)을 구해서 이 시간이 정답이 될 수 있는지 테스트합니다.
        mid = (low + high) // 2

        current_sum = 0
        for s in servers:
            # min(s, mid)와 같은 로직이지만 if문이 파이썬에서 미세하게 더 빠릅니다.
            if s > mid:
                current_sum += mid
            else:
                current_sum += s

        # 목표치 이상으로 켜졌다면, 시간을 더 줄여볼 수 있는지 확인 (왼쪽 탐색)
        if current_sum >= limit_server:
            answer = mid  # 일단 현재 시간을 정답 후보로 저장
            high = mid - 1
        # 목표치에 미달했다면, 시간이 더 필요함 (오른쪽 탐색)
        else:
            low = mid + 1

    print(answer)


# 함수 실행
solve()