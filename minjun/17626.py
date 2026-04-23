lag_dict = {num*num:1 for num in range(223, 0, -1)}
sq_nums = list(lag_dict.keys())

# num의 제곱수 합의 최소 개수
def lagrangju(n):
    if lag_dict.get(n, False):
        return lag_dict[n]
    
    answer = 1e9
    for sq_num in sq_nums:
        if n == sq_num:
            return 1
        if n > sq_num:
            answer = min(answer, 1 + lagrangju(n-sq_num))
    
    lag_dict[n] = answer
    return answer

n = int(input())
print(lagrangju(n))