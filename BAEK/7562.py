from collections import deque

def BFS(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= l or ny < 0 or ny >= l:
        continue
      if board[nx][ny] == 0:
        board[nx][ny] = board[x][y] + 1
        queue.append((nx, ny))

  return board[finish_x][finish_y]



T = int(input())

result = [0] * T
for t in range(T):
  l = int(input())
  start_x, start_y = map(int, input().split())   # 나이트 시작 위치
  finish_x, finish_y = map(int, input().split())  # 나이트 목표 위치
  
  board = [[0] * l for _ in range(l)] # 체스판 2차원 배열
  dx = [-1, -2, -1, -2, 1, 2, 1, 2]   # 이동 가능한 모든 방향
  dy = [-2, -1, 2, 1, -2, -1, 2, 1]

  if start_x != finish_x or start_y != finish_y:    # 시작 위치와 목표 위치가 다를 때만 BFS 수행(같으면 0)
    result[t] = BFS(start_x, start_y)               # 몇 번 이동해야 하는지 test case 별로 결과 저장

for t in range(T):
  print(result[t])
