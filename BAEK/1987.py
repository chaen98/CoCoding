import sys

def DFS(y, x):
  global new
  global result

  if x < 0 or x >= C or y < 0 or y >= R:
    return

  if board[y][x] not in visited:
    visited.add(board[y][x])    # 밟는 동시에 지나온 칸으로 업데이트
    new += 1      # 칸 수 +1

    DFS(y-1, x)
    DFS(y+1, x)
    DFS(y, x-1)
    DFS(y, x+1)

    result = max(result, new)     # 최대 칸 수 업데이트
    visited.remove(board[y][x])   # 최대 칸 수가 아닐 경우 다시 백트래킹하기 위해 현재 칸을 지나지 않은 칸으로 만들어줌
    new -= 1      # 뒤로 돌아가기 때문에 지난 칸을 다시 -1 해줌

  return

R, C = map(int, input().split())
board = [list(map(str, sys.stdin.readline())) for _ in range(R)]

visited = set()   # 지나온 칸인지 지나지 않은 칸인지 저장(리스트 형일때 보다 훨씬 시간 단축 됨)
new, result = 0, 0
DFS(0, 0)         # 시작점이 (0, 0)이므로 (0, 0)부터 시작

print(result)
