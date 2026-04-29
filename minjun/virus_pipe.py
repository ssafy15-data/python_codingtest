def solution(n, infection, edges, k):
    maxval = [0]

    infected = [False] * (1+n)
    infected[infection] = True

    def oepn_pipe(pipe_num):
        new_infected = []

        # 모든 edge를 순회하며, 열린 파이프이면서 한쪽이 감염되고 한쪽이 감염되지 않은 경우, 감염처리
        # 그런데 같은 파이프 종류가 연속해서 연결된 경우, 연쇄 전파 처리가 안 되어있는 구조이기 때문에, while문 한번 더 돌기
        while True:
            again = False
            for n1, n2, p in edges:
                if p == pipe_num:
                    if infected[n1] and not infected[n2]:
                        infected[n2] = True
                        new_infected.append(n2)
                        again = True
                    elif infected[n2] and not infected[n1]:
                        infected[n1] = True
                        new_infected.append(n1)
                        again = True
            if not again:
                break
        return new_infected


    def recurr(k_num):
        if maxval[0] == n:
            # 이미 최대값 갱신이 된 경우 종료
            return
        if sum(infected) == n:
            # 이전 처리로 최대값 갱신이 된 경우 종료
            maxval[0] = n
            return
        if k_num == 0:
            # 최대 횟수만큼 열고 닫은 경우, 최대값 갱신하고 종료
            maxval[0] = max(maxval[0], sum(infected))
            return

        for i in range(1, 4):
            new_infected = oepn_pipe(i)
            recurr(k_num-1)
            # 감염되었던것 감염 안된 처리하기
            for node in new_infected:
                infected[node] = False

    recurr(k)    
    return maxval[0]