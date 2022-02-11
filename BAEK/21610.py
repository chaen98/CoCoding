N, M = map(int, input().split())
sky = [list(map(int, input().split())) for _ in range(N)]
ds = [list(map(int, input().split())) for _ in range(M)]

clouds = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]

dz = [-1, -1, 1, 1]
dw = [-1, 1, -1, 1]

for m in range(M):
  d, s = ds[m][0], ds[m][1]     # 이동 방향, 횟수

  visited = [[False] * N for _ in range(N)]
  new_cloud = []

  # 1. 구름 이동
  for cloud in clouds:
    c_y, c_x = cloud[0], cloud[1]

    c_y = (c_y + (dy[d] * s)) % N
    c_x = (c_x + (dx[d] * s)) % N
    new_cloud.append([c_y, c_x])    # 새로운 위치에 구름 생성

    # 2. 물의 양 1씩 증가
    sky[c_y][c_x] += 1
    visited[c_y][c_x] = True


  # 3. 구름 사라짐
  clouds = []


  # 4. 대각선 바구니 만큼 물의 양 증가
  for cloud in new_cloud:
    c_y, c_x = cloud[0], cloud[1]
    cnt = 0

    for i in range(4):    # 대각선 모두 확인
      ny = c_y + dz[i]
      nx = c_x + dw[i]

      if 0 <= nx < N and 0 <= ny < N and sky[ny][nx] > 0:     # 범위 내에 있고 0 이상이라면
        cnt += 1
    
    sky[c_y][c_x] += cnt


  # 5. 기존 구름이 있던 칸을 제외하고 물의 양 2이상인 칸이 존재한다면 2씩 감소 & 구름 생성
  for i in range(N):
    for j in range(N):
      if sky[i][j] >= 2 and visited[i][j] == False:
        sky[i][j] -= 2
        clouds.append([i, j])



result = 0
for s in sky:
  result += sum(s)

print(result)
