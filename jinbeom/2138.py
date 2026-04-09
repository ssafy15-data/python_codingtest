n = int(input())
arr1 = input()
arr2 = input()
if arr1[0] != arr2[0]:
    prev1 = [0, 1]
    prev2 = [1, 0]
    ret1 = 1
    ret2 = 1
else:
    prev1 = [0, 0]
    prev2 = [1, 1]
    ret1 = 0
    ret2 = 2
for idx in range(1, n - 1):
    if arr1[idx] != arr2[idx]:
        ret1 += 1 - (prev1[idx] + prev1[idx - 1]) % 2
        prev1.append(1 - (prev1[idx] + prev1[idx - 1]) % 2)
        ret2 += 1 - (prev2[idx] + prev2[idx - 1]) % 2
        prev2.append(1 - (prev2[idx] + prev2[idx - 1]) % 2)
    else:
        ret1 += (prev1[idx] + prev1[idx - 1]) % 2
        prev1.append((prev1[idx] + prev1[idx - 1]) % 2)
        ret2 += (prev2[idx] + prev2[idx - 1]) % 2
        prev2.append((prev2[idx] + prev2[idx - 1]) % 2)

if (prev1[n - 1] + prev1[n - 2] + int(arr1[n - 1]) - int(arr2[n - 1])) % 2:
    if (prev2[n - 1] + prev2[n - 2] + int(arr1[n - 1]) - int(arr2[n - 1])) % 2:
        print(-1)
    else:
        print(ret2)
else:
    if (prev2[n - 1] + prev2[n - 2] + int(arr1[n - 1]) - int(arr2[n - 1])) % 2:
        print(ret1)
    else:
        print(min(ret1, ret2))
