def Curve(x, y):
  # 세대 수 만큼 반복
  for i in range(g):
    for j in range(len(direction) - 1, -1, -1):      # 방향 좌표 리스트 뒤에서부터 하나씩
      direction.append((direction[j] + 1) % 4)      # 1을 더한 후 4로 나누어 다음 방향좌표 저장

  for d in direction:      # 저장된 방향좌표에 따라 드래곤 커브로 변경(방문처리)
    y += dy[d]
    x += dx[d]

    if 0 <= x <= 100 and 0 <= y <= 100:    # 범위를 벗어나지 않은 경우에만
      board[y][x] = True



N = int(input())
board = [[False] * 101 for _ in range(101)]

# 방향 0, 1, 2, 3
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

# 드래곤 커브 종류 순서대로
for _ in range(N):
  x, y, d, g = map(int, input().split())
  board[y][x] = True    # 시작지점을 드래곤 커브로 변경(= 방문처리)
  direction = [d]

  Curve(x, y)      # 드래곤 커브 수행

# 드래곤 커브 개수 세기
result = 0
for i in range(100):
  for j in range(100):
    if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
      result += 1

print(result)




# 인덱스에러 5번... 범위 잘 보고 쓸 것!!!
