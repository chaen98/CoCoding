import sys
sys.setrecursionlimit(10**6)

T = int(input())

lst = []


def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0

        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        return True
    return False


for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    result = 0
    for i in range(N):
        for j in range(M):
            if DFS(i, j) == True:
                result += 1

    lst.append(str(result))

print('\n'.join(lst))
