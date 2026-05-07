N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0
for idx in range(N):
    current_num = numbers[idx]
    low = 0
    high = N - 1
    while low < high:
        if low == idx:
            low += 1
            continue
        if high == idx:
            high -= 1
            continue
        #(current_num, numbers[low], numbers[high])
        test_num = numbers[low] + numbers[high]
        if test_num == current_num:
            count += 1
            break
        elif test_num < current_num:
            low += 1
        else:
            high -= 1


print(count)