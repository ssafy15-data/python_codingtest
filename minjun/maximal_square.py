# 시간초과...

matrix = [[0 if matrix[i][j] == "0" else 1 for j in range(len(matrix[0])) ] for i in range(len(matrix))]
m = len(matrix)
n = len(matrix[0])

max_n = 0

def is_bigger(trying_n, tried_n, i, j):
    for k in range(tried_n, trying_n):
        if matrix[i+k][j+k] == "0":
            return False
        for s in range(k):
            if matrix[i+s][j+k] == "0" or matrix[i+k][j+s] == "0":
                return False
    return True

for i in range(m):
    if (i+max_n) >= m:
        break
    for j in range(n):
        if (j+max_n) >= n or (i+max_n) >= m:
            break
        tried_n = 0
        if matrix[i][j] == "1":
            while True:
                if is_bigger(max_n+1, tried_n, i, j):
                    max_n += 1
                    tried_n = max_n
                    if (i+max_n) >= m or (j+max_n) >= n:
                        break
                else:
                    break
print(max_n)