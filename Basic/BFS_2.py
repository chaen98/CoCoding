# 미로 탈출

from collections import deque

def BFS(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if maze[nx][ny] == 0:
        continue
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))
  return maze[N-1][M-1]
      

N, M = map(int, input().split())

maze = []
for _ in range(N):
  maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(BFS(0, 0))
