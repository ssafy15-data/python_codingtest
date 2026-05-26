import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent_dict = {i:i for i in range(n)}

def enroll_relation(node1, node2):
    parent1 = find_parent(node1)
    parent2 = find_parent(node2)
    
    if parent1 == parent2:
        pass
    elif parent1 < parent2:
        parent_dict[parent2] = parent1
    else:
        parent_dict[parent1] = parent2

def find_parent(num):
    temp_parent = parent_dict[num]
    if temp_parent == num:
        return num
    parent_dict[num] = find_parent(temp_parent)
    return parent_dict[num]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(i+1, n):
        if line[j] == 1:
            enroll_relation(i, j)

plan = list(map(int, input().split()))

answer = "YES"
for i in range(len(plan)-1):
    if find_parent(plan[i]-1) != find_parent(plan[i+1]-1):
        answer = "NO"
        break
print(answer)