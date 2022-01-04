N, K = map(int, input().split())

lst = []
for _ in range(N):
  lst.append(list(map(int, input().split())))

rank = [0] * (N+1)

lst.sort(key = lambda x:(-x[1], -x[2], -x[3]))    # 금, 은, 동 많은 순(역순)으로 정렬

for i in range(1, N+1):
  rank[lst[i-1][0]] = i   # 1번 국가는 rank[1]에 등수 저장, 2번 국가는 rank[2]에 등수 저장
  if i > 1 and i < N+1:
    for j in range(i-2, -1, -1):    # 앞 등수의 국가와 메달 수가 같은지 확인
      if lst[i-1][1] == lst[j][1] and lst[j][2] == lst[j][2] and lst[i-1][3] == lst[j][3]:
        rank[lst[i-1][0]] -= 1    # 같다면 등수를 -1 해주고 동일한 등수로 저장

# print(rank)
print(rank[K])
