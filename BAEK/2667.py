N = int(input())

def DFS(x, y):
    global count

    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1

        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True
    return False


graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

count = 0
result = []
for i in range(N):
    for j in range(N):
        if DFS(i, j) == True:
            result.append(count)
            count = 0

result.sort()
print(len(result))
for r in result:
    print(r)
