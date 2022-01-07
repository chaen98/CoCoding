import sys
sys.setrecursionlimit(100000)   # Python에서 기본 재귀 깊이는 1000인데, DFS(재귀함수)가 최대 100*100 = 100,000 번 반복될 수 있기 때문에 범위 늘려야 런타임 에러가 발생하지 않음

def DFS(y, x):
  global area

  if x < 0 or x >= N or y < 0 or y >= M:    # 영역을 벗어나면 리턴
    return False

  if paper[y][x] == 0:    # 한번도 방문하지 않은 경우
    area += 1             # 영역의 넓이 + 1 증가
    paper[y][x] = 1       # 방문처리

    DFS(y-1, x)           # 인접 영역 방문
    DFS(y+1, x)
    DFS(y, x-1)
    DFS(y, x+1)

    return True

  return False



M, N, K = map(int, input().split())     # 세로, 가로, 사각형 좌표

paper = [[0] * N for _ in range(M)]

for _ in range(K):
  left_x, left_y, right_x, right_y = map(int, input().split())

  for i in range(right_y - left_y):
    for j in range(right_x - left_x):
      paper[left_y + i][left_x + j] = 1   # 방문 불가(장애물) 영역으로 처리

area = 0
lst_area = []
for i in range(M):
  for j in range(N):
    if DFS(i, j) == True:
        lst_area.append(area)
        area = 0        # 영역 넓이 리셋

    
lst_area.sort()
a = ''
for l in lst_area:
  a += str(l) + ' '
print(len(lst_area), a[:-1], sep = '\n')    # a[:-1]: a 문자열의 마지막 문자 제거(마지막에 추가된 스페이스 문자를 제거하고 출력하기 위해서)
