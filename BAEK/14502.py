from itertools import combinations
import copy

def DFS(y, x):
  if x < 0 or x >= M or y < 0 or y >= N:
    return

  if lst_copy[y][x] == 0:
    lst_copy[y][x] = 2

    DFS(y-1, x)
    DFS(y+1, x)
    DFS(y, x-1)
    DFS(y, x+1)
    return

  return



N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

empty = []
for i in range(N):      # 빈 칸 확인
  for j in range(M):
    if lst[i][j] == 0:
      empty.append([i, j])

walls = list(combinations(empty, 3))      # 벽을 세울 수 있는 빈칸 종류
result = []

for wall in walls:      # 벽을 만드는 모든 경우의 수 확인
  lst_copy = copy.deepcopy(lst)     # 2차원 리스트 깊은 복사
  lst_copy[wall[0][0]][wall[0][1]] = 1
  lst_copy[wall[1][0]][wall[1][1]] = 1
  lst_copy[wall[2][0]][wall[2][1]] = 1

  for i in range(N):      # 바이러스가 있는 경우 DFS 수행
    for j in range(M):
      if lst_copy[i][j] == 2:
        lst_copy[i][j] = 0
        DFS(i, j)

  cnt = 0
  for i in range(N):      # 퍼지지 않은 곳 개수 카운트
    for j in range(M):
      if lst_copy[i][j] == 0:
        cnt += 1
  
  result.append(cnt)

print(max(result))


# 알고리즘 분류는 BFS로 되어있지만 DFS를 이용해서 풀었음.
