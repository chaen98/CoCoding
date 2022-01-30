import copy

def DFS(start, cctv, room):
  global result

  if start == len(cctv):      # 모든 cctv의 경우의 수를 다 판단하였을 경우
    cnt = 0

    for n in range(N):      # 0의 개수 세기
      for m in range(M):
        if room[n][m] == 0:
          cnt += 1

    result = min(result, cnt)     # 사각지대 최소값 저장
    return

  num, y, x = cctv[start]       # cctv 종류 & y좌표 & x좌표
  for dir in direction[num]:      # 90도 회전 시 가능한 모든 경우 검사
    tmp = copy.deepcopy(room)

    for d in dir:     # 감시 가능한 범위는 0을 #으로 변경
      ny = y + dy[d]
      nx = x + dx[d]

      while 0 <= ny < N and 0 <= nx < M:
        if tmp[ny][nx] == 6:      # 6일 때 바로 종료
          break
        elif tmp[ny][nx] == 0:
          tmp[ny][nx] = '#'

        ny = ny + dy[d]
        nx = nx + dx[d]

    DFS(start+1, cctv, tmp)     # cctv 종류 변경하고, 변경된 사무실 상태를 유지시켜 재귀



dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
direction = [0,                                               # cctv 종류별 90도 회전시 가능한 모든 방향
            [[0], [1], [2], [3]], 
            [[0, 1], [2, 3]],
            [[0, 3], [1, 3], [1, 2], [0, 2]],
            [[0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]],
            [[0, 1, 2, 3]]
            ]



if __name__ == "__main__":
  N, M = map(int, input().split())
  room = [list(map(int, input().split())) for _ in range(N)]
  
  cctv = []
  for i in range(N):
    for j in range(M):
      if room[i][j] != 0 and room[i][j] != 6:
        cctv.append([room[i][j], i, j])         # cctv 존재하는 곳 저장

  result = 65         # 사각지대 최소값 저장 변수(최대 8x8=64개의 사각지대 존재할 수 있음)
  DFS(0, cctv, room)
  print(result)
