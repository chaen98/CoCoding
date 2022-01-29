from collections import deque

# 방향변환 함수
def Change(dir):
  dir = (dir + 1) % 4
  return dir


# 로봇청소기 이동 함수
def Move(y, x):
  global d
  bNoway = True     # 더 이상 이동할 곳이 없는지 확인

  for k in range(4):      # 네 방향 모두 확인
    d = Change(d)     # 왼쪽으로 회전하기 위해 방향 변환

    ny = y + dy[d]
    nx = x + dx[d]

    if lst[ny][nx] == 0:      # 한번도 방문하지 않은 구역만 방문하도록
      bNoway = False      # 이동할 수 있는 곳이 존재함
      lst[ny][nx] = max(map(max, lst)) + 1      # 청소완료한 칸으로 +1 증가
      Move(ny, nx)      # 새로 이동한 좌표에서 다시 시작
      break

  if bNoway:      # 네 방향 모두 이동할 수 없는 경우
    back = Change(d+1)      # 후진해야 하기 때문에 방향 바꿔줌/ back 변수를 사용한 이유는 '바라보는 방향을 유지한 채로 후진'해야 하기 때문에 원래 방향변수 d는 변경하지 않고 새로운 변수 만듬
    ny = y + dy[back]
    nx = x + dx[back]

    if lst[ny][nx] == -1:     # 후진하는 곳이 벽이라면 종료
      return
    else:     # 벽이 아닐 경우 후진 가능
      Move(ny, nx)


# 상(북) 좌(서) 하(남) 우(동) -> 왼쪽으로 이동하기 때문에 반시계방향 회전
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

if __name__ == "__main__":
  N, M = map(int, input().split())    # 가로&세로
  r, c, d = map(int, input().split())     # 청소기 좌표&방향
  lst = [list(map(int, input().split())) for _ in range(N)]

  lst = [[-1 if l == 1 else 0 for l in row] for row in lst]     # 벽은 1로 주어지지만 -1로 바꾸어 저장
  if d == 1: d = 3      # 입력이 1(동쪽)인 경우 dy,dx 좌표에 맞추어 3으로 변경해줌/ 원래 입력대로 라면, 시계방향으로 회전하기 때문
  elif d == 3: d = 1

  lst[r][c] = 1     # 시작위치는 바로 청소완료한 칸으로 바꿔줌
  Move(r, c)      # 이동 시작
  print(max(map(max, lst)))



# 3190번과 유사한 문제라고 생각이 들었고, 그 때 코드를 생각하며 풀었음.
