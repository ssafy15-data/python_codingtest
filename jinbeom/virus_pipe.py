def solution(n, infection, edges, k):
    global ret
    answer = 0
    adj=[[set(),set(),set()] for _ in range(n)]
    visit=[[False]*3 for _ in range(n)]
    graph=[[set(),set(),set()] for _ in range(n)]
    for x,y,type in edges:
        graph[x-1][type-1].add(y-1)
        graph[y-1][type-1].add(x-1)
    for x in range(n):
        for idx in range(3):
            if visit[x][idx]: continue
            q=[x]
            visit[x][idx]=True
            tmp={x}
            while q:
                now=q.pop()
                for nxt in graph[now][idx]:
                    if not visit[nxt][idx]:
                        q.append(nxt)
                        visit[nxt][idx]=True
                        tmp.add(nxt)
            for y in tmp:
                adj[y][idx]=tmp
    ret=0

    def select_pipe(infected, prev, t):
        global ret
        if t==0:
            ret=max(ret,len(infected))
            return
        for idx in range(3):
            if idx==prev: continue
            tmp=set()
            for x in infected:
                tmp|=adj[x][idx]
            select_pipe(infected|tmp,idx,t-1)

    select_pipe({infection-1},-1,k)

    return ret
