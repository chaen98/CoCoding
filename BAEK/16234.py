from collections import deque

def BFS(y, x):
  queue = deque()
  result = 0
  cnt = 0
  lst = []
  global bcheck

  queue.append((y, x))
  lst.append((y, x))
  visited[y][x] = True

  while queue:
    y, x = queue.popleft()
    cnt += 1
    result += people[y][x]

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
      if visited[ny][nx] == True:
        continue
      if L <= abs(people[y][x] - people[ny][nx]) <= R:        # 인구 차이 확인
        visited[ny][nx] = True      # 방문처리
        queue.append((ny, nx))      # 국경선 열기
        lst.append((ny, nx))       # 국경선 열린 나라 좌표 저장
        bcheck = True     # 인구이동 가능하도록 True로 변경

  return result, cnt, lst     # 인구이동이 가능한 나라의 인구 합 / 인구이동이 가능한 나라 수 / 인구이동할 나라의 좌표 리스트


N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
while True:     # 인구이동이 가능하다면 계속 반복
  visited = [[False] * N for _ in range(N)]     # 방문처리 리스트 초기화
  bcheck = False      # 인구이동 가능여부 확인 변수 초기화

  for i in range(N):
    for j in range(N):    
      if visited[i][j] == False:      # 한 번도 방문하지 않은 곳만 방문
        result, cnt, lst = BFS(i, j)      # BFS 수행
        new = result // cnt     # 소수점 버림

        for l in lst:
          a, b = l[0], l[1]     # 인구이동할 나라의 y좌표, x좌표
          people[a][b] = new      # 인구이동 결과값 저장

  if not bcheck:      # 더 이상 이동이 불가능할 경우
    break

  answer += 1     # 인구이동 발생 횟수 카운트

print(answer)





# Python3: 시간초과 / PyPy3: 통과
