N, M = map(int,input().split())
lst = [int(input()) for _ in range(N)]
dp = [10001] * (M + 1)

dp[0] = 0
for i in lst:
  for j in range(i, M+1):
    if dp[j-i] != 10001:
      dp[j] = min(dp[j], dp[j-i] + 1)
    
if dp[M] == 10001:
  print(-1)
else:
  print(dp[M])
