import sys
input = sys.stdin.readline
import copy

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
for r in range(R):    # 공기청정기 위치 저장(cleaner[0]- 위쪽 / cleaner[1]- 아래쪽)
  if A[r][0] == -1:
    cleaner.append(r)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(T):
  dust = copy.deepcopy(A)    # 미세먼지 확산이 동시에 일어나기 때문에 값을 중간에 바뀐 값이 들어가지 않도록 복사해줌
  # 1. 미세먼지 확산
  for i in range(R):    # 각 칸을 돌면서
    for j in range(C):
      if A[i][j] > 0:    # 먼지가 존재하는 곳이라면
        tmp = A[i][j] // 5    # 먼지가 확산되는 양 저장하여
        
        for k in range(4):    # 인접한 곳에 먼지 확산시키기
          nx = j + dx[k]
          ny = i + dy[k]

          if 0 <= nx < C and 0 <= ny < R:    # 범위 내에 있을 때
            if A[ny][nx] == -1:    # 공기청정기 존재하면 pass
              continue
              
            dust[ny][nx] += tmp    # 확산된 먼지 저장
            dust[i][j] -= tmp    # 확산 후 남은 미세먼지 업데이트

            
  # 2. 공기청정기 작동
  pos_u = cleaner[0]    # 공기청정기 위쪽
  pos_d = cleaner[1]    # 공기청정기 아래쪽
  
  for u in range(pos_u-1, -1, -1):    # 공기청정기 위쪽 첫 열
    dust[u+1][0] = dust[u][0]
  for u in range(1, C):    # 공기청정기 위쪽 첫 행
    dust[0][u-1] = dust[0][u]
  for u in range(1, pos_u+1):    # 공기청정기 위쪽 마지막 열
    dust[u-1][C-1] = dust[u][C-1]
  for u in range(C-2, 0, -1):    # 공기청정기 위쪽 행
    dust[pos_u][u+1] = dust[pos_u][u]
  for d in range(pos_d+1, R):    # 공기청정기 아래쪽 첫 열
    dust[d-1][0] = dust[d][0]
  for d in range(1, C):    # 공기청정기 아래쪽 마지막 행
    dust[R-1][d-1] = dust[R-1][d]
  for d in range(R-2, pos_d-1, -1):    # 공기청정기 아래쪽 마지막 열
    dust[d+1][C-1] = dust[d][C-1]
  for d in range(C-2, 0, -1):    # 공기청정기 아래쪽 행
    dust[pos_d][d+1] = dust[pos_d][d]

  dust[pos_u][0], dust[pos_d][0] = -1, -1    # 공기청정기 위치는 다시 -1로 바꾸어줌
  dust[pos_u][1], dust[pos_d][1] = 0, 0    # 공기청정기로 들어간 자리는 먼지 제거

  A = copy.deepcopy(dust)    # 바뀐 미세먼지 값/위치 업데이트

result = 2    # 공기청정기 위치는 -1이 들어가있으므로 +2부터 시작
for d in dust:
  result += sum(d)

print(result)




# Python3- 시간초과 / PyPy3- 통과
