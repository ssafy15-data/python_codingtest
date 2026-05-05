def solution(n, infection, edges, k):
    adj = [[] for _ in range(n + 1)]
    for u, v, t in edges:
        adj[u].append((v, t))
        adj[v].append((u, t))

    infected = {infection}
    max_total_infected = 0

    def get_max_infected(current_infected, remaining_k):
        nonlocal max_total_infected

        max_total_infected = max(max_total_infected, len(current_infected))

        if remaining_k == 0 or len(current_infected) == n:
            return

        for pipe_type in range(1, 4):
            new_infected = set(current_infected)
            stack = list(current_infected)
            added = False
            while stack:
                curr = stack.pop()
                for neighbor, t in adj[curr]:
                    if t == pipe_type and neighbor not in new_infected:
                        new_infected.add(neighbor)
                        stack.append(neighbor)
                        added = True

            if added:
                get_max_infected(new_infected, remaining_k - 1)
            else:
                max_total_infected = max(max_total_infected, len(new_infected))

    get_max_infected(infected, k)
    return max_total_infected
