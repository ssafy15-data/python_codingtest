import math

N = int(input())


if int(math.sqrt(N)) ** 2 == N:
    print(1)
    exit()

for i in range(1, int(math.sqrt(N)) + 1):
    left = N - i ** 2
    if int(math.sqrt(left)) ** 2 == left:
        print(2)
        exit()

for i in range(1, int(math.sqrt(N)) + 1):
    for j in range(1, int(math.sqrt(N - i ** 2)) + 1):
        left = N - i ** 2 - j ** 2
        if int(math.sqrt(left)) ** 2 == left:
            print(3)
            exit()

print(4)