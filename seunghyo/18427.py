N, M, H = map(int, input().split())

blocks = [[0 for _ in range(H+1)] for _ in range(N+1)]
blocks[0][0] = 1

for student in range(1, N+1):
    new_blocks = list(map(int, input().split()))

    blocks[student] = blocks[student-1].copy()

    for i in range(H+1):
        if blocks[student-1][i] == 0:
            continue
        else:
            for block in new_blocks:
                if i + block <= H:
                    blocks[student][i+block] += blocks[student-1][i]
                    blocks[student][i + block] % 10007

    #print(blocks)


print(blocks[N][H] % 10007)