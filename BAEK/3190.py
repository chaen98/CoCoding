from collections import deque

# 방향 변환
def Change(d, c):
  if c == 'L':
    d = (d - 1) % 4
  else:
    d = (d + 1) % 4
  return d

# 우 하 좌 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

queue = deque()

# 뱀 이동
def Move():
  direction = 0   # 초기방향: 오른쪽
  sec = 1     # 시간
  y, x = 0, 0     # 초기 위치
  queue.append([y, x])      # 뱀이 존재하는 곳
  board[y][x] = -1      # 부딪히는 경우: -1

  while True:
    y = y + dy[direction]
    x = x + dx[direction]

    if 0 <= x < N and 0 <= y < N and board[y][x] != -1:
      if not board[y][x] == 1:      # 사과가 존재하지 않는 경우
        ny, nx = queue.popleft()      # 길이 줄이기
        board[ny][nx] = 0
      board[y][x] = -1      # 뱀 이동했으므로 업데이트
      queue.append([y, x])

      if sec in time_check.keys():      # 방향 바꿔야한다면
        direction = Change(direction, time_check[sec])
      sec += 1

    else:     # 벽에 부딪히는 경우, 자신의 몸과 부딪히는 경우
      return sec


if __name__ == "__main__":
  N = int(input())      # 보드의 크기
  K = int(input())      # 사과 위치
  board = [[0] * N for _ in range(N)]   # 보드 만들기

  for _ in range(K):      # 사과 위치 받기
    a, b = map(int, input().split())
    board[a-1][b-1] = 1     # 사과 위치 = 1

  L = int(input())      # 방향 변환 정보
  time_check = {}     # 딕셔너리 형태로 저장
  for _ in range(L):
    X, C = input().split()
    time_check[int(X)] = C

  print(Move())     # 뱀 이동
