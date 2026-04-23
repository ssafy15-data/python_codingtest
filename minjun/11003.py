# 시간초과

n, l = map(int, input().split())
nums = list(map(int, input().split()))
nums = [(num, idx) for idx, num in enumerate(nums)]
nums.sort(key=lambda x: x[0])

answers = [0] * n
start_dict = {i:i for i in range(n)}
end_dict = {i:i for i in range(n)}

def find_parent(dic, num):
    if num >= n:
        num = n-1
    elif num < 0:
        num = 0
    
    if dic[num] == num:
        return num
    dic[num] = find_parent(dic, dic[num])
    return dic[num]

for num, idx in nums:
    start = find_parent(start_dict, idx)
    end = find_parent(end_dict, idx+l-1)

    next_start = find_parent(start_dict, end+1)
    next_end = find_parent(end_dict, start-1)

    for i in range(start, end+1):
        answers[i] = num
        start_dict[i] = next_start
        end_dict[i] = next_end

print(*answers)

# start 지점을 잡을 때는, 오른쪽 빈칸으로
# end 지점을 잡을 때는, 왼쪽 빈칸으로

# start 찾을 때, dict에서 찾음 ()
# 해당 시점의 start 등록할 때, (해당 칸을 start 지점으로 잡으려는 경우, 안내하는 지점)
# 해당 시점의 end+1 칸에서 start dict 를 확인 (start_dict는 항상 빈칸을 안내)
# 빈 칸 여부는 dict에서 idx와 value의 일치 여부임