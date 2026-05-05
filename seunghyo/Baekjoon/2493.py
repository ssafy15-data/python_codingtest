N = int(input())
towers = list(map(int, input().split()))
answer = [0]
stacks = [(towers[0], 1)]

for idx in range(1, N):
    current_height = towers[idx]
    while stacks:
        if stacks[-1][0] >= current_height:
            answer.append(stacks[-1][1])
            break
        else:
            stacks.pop()

    if not stacks:
        answer.append(0)

    stacks.append((current_height, idx + 1))

print(" ".join(map(str, answer)))