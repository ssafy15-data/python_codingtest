n = int(input())
nums = list(map(int, input().split()))
nums_dict = {}

zero_cnt = 0
sum_dict = {}
for i in range(n):
    num_i = nums[i]
    if nums_dict.get(num_i, False):
        nums_dict[num_i] += 1
    else:
        nums_dict[num_i] = 1

    if num_i == 0:
        zero_cnt += 1
        continue

    for j in range(i+1, n):
        
        num_j = nums[j]
        if num_j == 0:
            continue
        sumnum = nums[i] + nums[j]
        sum_dict[sumnum] = True

answer = 0
for num in nums:
    if sum_dict.get(num, False):
        answer += 1
    elif zero_cnt > 0 and nums_dict[num] > 1:
        answer += 1
        if num == 0 and zero_cnt < 3:
            answer -= 1
    
print(answer)