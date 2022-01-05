from collections import deque


def BFS():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        dx = [x - 1, x + 1, x * 2]

        if x == K:
            return graph[x]

        for i in range(3):
            nx = dx[i]
            if 0 <= nx <= 100000 and not graph[nx]:
                graph[nx] = graph[x] + 1
                queue.append(nx)


N, K = map(int, input().split())

graph = [0] * 100001
# graph[N] = 1

print(BFS())
