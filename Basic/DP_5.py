## 정답 예시 코드 ##
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))



## 내 코드 ##
N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
  for j in range(i-1, -1, -1):
    if lst[i] <= lst[j]:
      dp[i] = max(dp[j] + 1, dp[i])
      break
    else:
      dp[i] = dp[i-1]
    print(dp)

print(N - dp[N-1])
