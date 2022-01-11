from collections import deque

def BFS():
  while queue:
    y, x = queue.popleft()

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if nx < 0 or nx >= width or ny < 0 or ny >= height:
        continue
      if lst[ny][nx] == 'W':
        continue
      if lst[ny][nx] == 'L' and hour[ny][nx] == 0:    # 육지이면서 한 번도 방문하지 않았을 때
        hour[ny][nx] = hour[y][x] + 1
        queue.append((ny, nx))



queue = deque()

height, width = map(int, input().split())
lst = []    # 보물섬 지도 리스트
data = []   # L(육지)의 위치 저장을 위한 리스트
for h in range(height):
  lst.append(list(map(str, input())))
  for w in range(width):
    if lst[h][w] == 'L':    # 입력된 지도 리스트에서 L이 있다면 위치 저장
      data.append((h, w))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for d in data:    # 모든 L 지점에서 각각 BFS 수행
  hour = [[0]*width for _ in range(height)]
  queue.append(d)
  hour[d[0]][d[1]] = 1    # 바로 다음 칸이 보물이 있는 칸일 때, 0으로 하면 다시 시작지점으로 돌아가서 2가 정답이 되기 때문에 1부터 시작
  BFS()

  maximum = max(map(max, hour))   # 해당 L 위치에서 보물까지 걸리는 시간 저장
  result = max(result, maximum)   # 더 오래 걸리는 시간이 있다면 가장 큰 값으로 변경

print(result-1)   # hour[y][x] 시작 지점부터 +1 을 해주었기 때문에 마지막에 다시 -1
