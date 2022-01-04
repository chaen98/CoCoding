def DFS(start):
    global count
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            DFS(i)
            count += 1
            



num = int(input())
pair = int(input())

graph = [[] for _ in range(num+1)]
for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (num + 1)

count = 0
DFS(1)
print(count)
