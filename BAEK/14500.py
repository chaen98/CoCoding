def DFS(y, x, cnt, result):
  global ans

  if result + max_val * (4 - cnt) <= ans:     # 남은 사각형 값이 모두 최댓값이라해도 현재의 최대를 넘길 수 없다면, 즉시 종료
    return

  if cnt >= 4:      # 4개의 사각형을 모두 선택했다면, 값 확인 후 종료
    ans = max(ans, result)
    return
  
  for k in range(4):      # 좌우상하 이동
    ny = y + dy[k]
    nx = x + dx[k]

    if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
      if cnt == 2:      # ㅗ자 모양을 만들기 위해, 2개의 사각형을 모두 골랐다면 다시 자기 자기자신을 시작으로 하는 dfs를 호출
        visited[ny][nx] = 1
        DFS(y, x, cnt + 1, result + papers[ny][nx])
        visited[ny][nx] = 0
        
      visited[ny][nx] = 1
      DFS(ny, nx, cnt + 1, result + papers[ny][nx])
      visited[ny][nx] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if __name__ == "__main__":
  N, M = map(int, input().split())    # 세로, 가로
  papers = [list(map(int, input().split())) for _ in range(N)]
  max_val = max(map(max, papers))     # 종이 위에 쓰인 값 중 최대값 

  visited = [[0] * M for _ in range(N)]
  ans = 0

  for i in range(N):
    for j in range(M):
      visited[i][j] = 1
      DFS(i, j, 1, papers[i][j])
      visited[i][j] = 0

  print(ans)
