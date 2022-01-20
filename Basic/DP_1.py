## 정답 예시 코드 ##
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])




## 내 코드 ##
N = int(input())
K = list(map(int, input().split()))
dp = [0] * (N + 1)

dp[N-1] = K[N-1]
for n in range(N-2, -1, -1):
  dp[n] = max(dp[n + 1], K[n] + dp[n + 2])

print(dp[0])
