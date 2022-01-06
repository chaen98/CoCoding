import sys

def DFS(x):
  visited[x] = True

  for i in graph[x]:
    if not visited[i]:    # 연결되어 있음에도 방문하지 않은 경우 DFS 수행하여 방문처리
      DFS(i)



N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = list(map(int, sys.stdin.readline().split()))
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N + 1)
result = 0

for i in range(1, N+1):
  if visited[i] == False:   # 방문하지 않았을 경우 모든 정점을 방문하도록 DFS 수행
    DFS(i)
    result += 1
  

print(result)



# Python3로 실행한 경우 시간초과
# PyPy3로 변경 &
# a, b = list(map(int, input().split())) -> a, b = list(map(int, sys.stdin.readline().split())) 으로 변경
# BFS로도 풀이 가능함
