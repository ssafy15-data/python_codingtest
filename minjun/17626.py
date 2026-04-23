# 특정 수를 제곱수 합으로 표현할 때의 최소 개수 (메모이제이션)
lag_dict = {num*num:1 for num in range(223, 0, -1)}

# 223의 제곱부터 1의 제곱이 저장된 223개의 리스트
sq_nums = list(lag_dict.keys())

# num의 제곱수 합의 최소 개수 (재귀+메모이제이션)
def lagrangju(n):

    # 이미 저장되어 있다면 return
    if lag_dict.get(n, False):
        return lag_dict[n]
    
    # 최소 개수 초기화
    answer = 1e9
    
    # 223의 제곱부터 1의 제곱까지 순회하며,
    # n과 같아지거나 더 커지는 순간부터 최소개수 탐색 시작
    for sq_num in sq_nums:
        if n == sq_num:
            return 1
        if n > sq_num:
            answer = min(answer, 1 + lagrangju(n-sq_num))
    
    # 결과를 저장하고 후에 재사용
    lag_dict[n] = answer
    return answer

n = int(input())
print(lagrangju(n))