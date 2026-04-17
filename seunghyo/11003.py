import sys

def solve():
    input = sys.stdin.readline
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    current_min = A[0]
    current_count = 1
    D = [current_min]

    for idx in range(1, L):
        if A[idx] < current_min:
            current_min = A[idx]
        D.append(current_min)

    for idx in range(L, N):
        next_d = A[idx]
        out_d = A[idx - L]

        if current_min == out_d:
            if current_count == 1:
                current_min = min(A[idx-L+1:idx])
            else:
                current_count -= 1

        if next_d < current_min:
            current_min = next_d
            current_count = 1

        D.append(current_min)
        #print(idx, A[idx-L:idx], current_min)

    print(*D)
solve()