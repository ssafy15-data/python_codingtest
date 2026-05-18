from collections import deque

def cal_level(node):
    if levels[node] == -1:

        level = 1
        prev_parent = node
        prev_parents = [node]

        while True:
            parent = parents[prev_parent-2]
            if parent == 1:
                break
            elif levels[parent] != -1:
                level = level + levels[parent]
                break
            else:
                prev_parent = parent
                prev_parents.append(prev_parent)
                level += 1

        for idx, prev_parent in enumerate(prev_parents):
            levels[prev_parent] = level - idx

    return levels[node]

def cal_dist(node1, node2):
    dist = 0
    level_node1 = cal_level(node1)
    level_node2 = cal_level(node2)
    if level_node1 < level_node2:
        while level_node1 != level_node2:
            dist += 1
            node2 = parents[node2-2]
            level_node2 -= 1
    else:
        while level_node2 != level_node1:
            dist += 1
            node1 = parents[node1-2]
            level_node1 -= 1
    if node1 == node2:
        return dist
    else:
        while node1 != node2:
            node1 = parents[node1-2]
            node2 = parents[node2-2]
            dist += 2
        return dist
    
T = 1
for test_case in range(1, T+1):
    N = 11
    parents = [1, 1, 3, 3, 2, 4, 1, 3, 2, 9]
    graph = [[] for _ in range(N+1)]
    for idx, parent in enumerate(parents):
        graph[parent].append(idx+2)
    levels = [-1] * (N+1)
    levels[1] = 0

    answer = 0

    q = deque([1])
    node = 1
    while q:
        prev_node = node
        node = q.popleft()

        answer += cal_dist(prev_node, node)

        for child in graph[node]:
            q.append(child)

    print(f"#{test_case} {answer}")