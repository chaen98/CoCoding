for _ in range(int(input())):
  n, m = map(int, input().split())
  lst = list(map(int, input().split()))
  dp = [lst[x:x+m] for x in range(0, len(lst), m)]
  
  for i in range(1, m):
    for j in range(n):
      if j == 0:
        dp[j][i] = dp[j][i] + max(dp[j][i-1], dp[j+1][i-1])
      elif j == n-1:
        dp[j][i] = dp[j][i] + max(dp[j-1][i-1], dp[j][i-1])
      else:
        dp[j][i] = dp[j][i] + max(dp[j-1][i-1], dp[j][i-1], dp[j+1][i-1])
    
  print(dp)
  print(max(map(max, dp)))
