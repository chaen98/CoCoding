from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []      # 집 좌표
chicken = []      # 치킨집 좌표
for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      house.append([i, j])
    elif city[i][j] == 2:
      chicken.append([i, j])


data = list(combinations(chicken, M))     # 치킨집을 M개 선택하는 모든 경우의 수

result = []
for d in data:      # 모든 경우의 수를 검사
  sum_dist = 0

  for h in house:     # 한 집씩 가까운 치킨집 거리 계산
    min_dist = 100

    for k in range(len(d)):
      dist = abs(h[0] - d[k][0]) + abs(h[1] - d[k][1])
      min_dist = min(min_dist, dist)

    sum_dist +=  min_dist     # 모든 집의 치킨거리 계산

  result.append(sum_dist)     # 결과리스트에 저장

print(min(result))      # 결과리스트 중 제일 작은 값 출력
