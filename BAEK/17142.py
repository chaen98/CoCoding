import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
import copy

def BFS():
  cnt = 0
  while queue:
    if cnt >= empty:    # 0(빈칸)인 공간을 모두 채웠음에도 불구하고 큐에 활성화된 바이러스가 남아있을 경우 오답출력을 막기 위함
      return    # 0인 곳의 개수만큼 0인 곳을 방문했다면 리턴
    
    y, x = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= N:    # 범위를 넘어가는 경우
        continue
      if lab[ny][nx] == 0:    # 빈칸인 경우 바이러스 확산 후 큐에 삽입
        lab[ny][nx] = lab[y][x] + 1
        cnt += 1    # 0인 곳 방문 횟수 증가
        queue.append((ny, nx))
      if lab[ny][nx] == '*':    # 비활성화 바이러스인 경우 바이러스 확산 후 큐에 삽입
        lab[ny][nx] = lab[y][x] + 1
        queue.append((ny, nx))
    
  

N, M = map(int, input().split())
laboratory, virus = [], []    # 연구실 지도 & 바이러스 위치
ans = N * N    # 정답 초기화
empty = 0    # 0(빈칸)인 곳의 개수

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for n in range(N):
  lst = list(map(int, input().split()))
  for l in range(N):
    if lst[l] == 0:    # 0인 곳의 개수 카운트
      empty += 1
    if lst[l] == 1:    # 벽인 곳을 '-'로 변경
      lst[l] = '-'
    elif lst[l] == 2:    # 바이러스 위치인 곳을 '*'로 변경
      lst[l] = '*'
      virus.append((n, l))    # 바이러스 위치 리스트에 삽입
  laboratory.append(lst)

data = list(combinations(virus, M))    # 바이러스 리스트에서 활성화시킬 바이러스 M개를 선택하는 경우의 수 저장

for d in data:    # 모든 경우의 수 확인
  queue = deque()
  lab = copy.deepcopy(laboratory)

  for m in range(M):    # M개의 바이러스를 모두
    a = d[m][0]
    b = d[m][1]
    lab[a][b] = 1    # 활성화 시킨 후

    queue.append((a, b))    # 큐에 삽입

  BFS()    # BFS 수행
  
  flag = True
  result = 0
  for i in range(N):    # 모든 칸을 돌면서
    for j in range(N):
      if lab[i][j] == 0:    # 바이러스가 확산되지 못한 곳이 있다면
        flag = False    # 최소시간 업데이트 하지 않음
        break
      if str(type(lab[i][j])) == "<class 'int'>":    # 리스트에 저장된 값이 int 자료형인 경우에만
        result = max(result, lab[i][j])    # 확산하는데에 걸린 시간 저장

  if flag:    # 바이러스 확산이 모든 곳에 이루어졌다면
    ans = min(result, ans)    # 최소시간 업데이트
  
print(ans-1 if ans < N*N else -1)    # 최소시간 업데이트가 이루어지지 않았다면, 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우이므로 -1 출력





# 처음에 틀린 이유:
# 활성화 바이러스가 비활성화 바이러스를 만났을 때 활성화로 변경해주는 부분 없었음
# 빈 칸을 모두 채웠음에도, 큐에 먼저 들어와있던 활성화된 비활성화 바이러스가 여전히 큐에 남아있게 되어 BFS를 한 번 더 수행해버림(정답 최소시간보다 더 큰 최소시간 출력함)
# ex) 5 1
#     0 2 2 2 2
#     0 1 2 2 2
#     0 1 2 2 2
#     0 1 2 2 2
#     0 1 2 2 1
# 정답: 5, 오답: 6
