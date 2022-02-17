from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())    # 땅 크기 / 나무 수 / K년 후
ground = [[5] * N for _ in range(N)]      # 모든 땅에 양분 5씩 초기화
nutrient = [tuple(map(int, input().split())) for _ in range(N)]    # 각 칸마다 겨울에 추가되는 양분의 수
tree = [[deque() for _ in range(N)] for _ in range(N)]      # 각 칸 별로 나무의 나이 저장
for _ in range(M):
  x, y, z = map(int, input().split())
  tree[x-1][y-1].append(z)    # (1, 1)부터 시작하므로 1뺀 후 나이 저장

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for _ in range(K):
  # 봄 & 여름
  for i in range(N):
    for j in range(N):   
      for k in range(len(tree[i][j])):    # 봄: 칸 별로 존재하는 나무의 수만큼
        if ground[i][j] >= tree[i][j][k]:    # 해당 나무의 나이보다 양분이 많은 경우
          ground[i][j] -= tree[i][j][k]      # 양분 섭취
          tree[i][j][k] += 1      # 나이 증가

        else:    # 여름: 해당 나무부터 마지막 나무까지는 양분을 먹지 못하므로(이미 정렬 되어있기 때문에 하나씩 체크할 필요 x)
          for _ in range(k, len(tree[i][j])):
            ground[i][j] += (tree[i][j].pop() // 2)      # 나무 하나씩 pop해서 나이를 2로 나누고 양분으로 추가
          break    # 마지막 나무까지 처리했으므로 바로 여름 종료

  # 가을 & 겨울
  for i in range(N):
    for j in range(N):
      for k in tree[i][j]:    # 가을: 칸 별로 존재하는 나무 순서대로
        if k % 5 == 0:      # 나무의 나이가 5의 배수라면
          for l in range(8):
            nx = i + dx[l]
            ny = j + dy[l]
    
            if 0 <= nx < N and 0 <= ny < N:
              tree[nx][ny].appendleft(1)      # 인접한 칸에 나무 번식

      ground[i][j] += nutrient[i][j]    # 겨울: 땅에 양분 추가


result = 0
for i in range(N):
  for j in range(N):
    result += len(tree[i][j])    # 각 칸 별로 나무의 수 계산
print(result)




# 시간초과 6번
# 다른 코드 봄 / 다시 봐야 함
# 처음 나무 입력받을 때 한 위치에는 한 나무만 있기 때문에 처음에는 정렬할 필요 없음
# 그 후 가을에 번식을 하더라도 나무 리스트 가장 왼쪽에 넣어주기 때문에 자동 정렬 됨
