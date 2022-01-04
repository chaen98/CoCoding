from collections import deque

def DFS(V):
    visited0[V] = True
    print(V, end = ' ')
    for v in graph[V]:
        if not visited0[v]:
            DFS(v)
    
def BFS(V):
    queue = deque([V])
    visited1[V] = True
    
    while queue:
        x = queue.popleft()
        print(x, end = ' ')
        for v in graph[x]:
            if not visited1[v]:
                queue.append(v)
                visited1[v] = True
    
    
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited0 = [False] * (N + 1)
visited1 = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

DFS(V)
print()
BFS(V)
print()
