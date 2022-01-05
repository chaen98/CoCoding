N, S, P = map(int, input().split())
if N > 0: scores = [int(s) for s in input().split()]
else: scores = []

scores.append(S)
scores.sort(reverse = True)

if N == P and S <= scores[N]:
  print(-1)
  exit()

rank = [0] * (N + 1)
for i in range(N+1):
  rank[i] = i + 1
  if i > 0:
    for j in range(i-1, -1, -1):
      if scores[i] == scores[j]:
        rank[i] -= 1

r = scores.index(S)

if r < P:
  print(rank[r])
else:
  print(-1)
