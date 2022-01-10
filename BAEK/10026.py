import sys
sys.setrecursionlimit(10000)    # N이 최대 100 이므로 100*100 = 10000까지 가능하도록

def DFS(x, y):
  if x < 0 or x >= N or y < 0 or y >= N:
    return False

  if visited[x][y] == 0:      # 한 번도 방문하지 않으면 방문할 수 있도록
    if lst[x][y] == color:    # 같은 색 영역일 경우에만 방문 & true 리턴
      visited[x][y] = 1       # 방문 완료

      DFS(x-1, y)
      DFS(x+1, y)
      DFS(x, y-1)
      DFS(x, y+1)
      return True

  return False



N = int(input())
lst = [list(map(str, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

result_1 = 0                  # 적록색맹이 아닌 경우
for i in range(N):
  for j in range(N):
    color = lst[i][j]
    if DFS(i, j) == True:
      result_1 += 1

lst = [['R' if r == 'G' else r for r in row] for row in lst]      # G를 모두 R로 바꾸기
visited = [[0] * N for _ in range(N)]

result_2 = 0                # 적록색맹인 경우
for i in range(N):
  for j in range(N):
    color = lst[i][j]
    if DFS(i, j) == True:
      result_2 += 1

print(result_1, result_2)
