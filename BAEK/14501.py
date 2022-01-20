N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]   # 상담 일정표
dp = [0] * (N + 1)      # dp 테이블 만들기

for i in range(N-1, -1, -1):
  if i + lst[i][0] > N:   # 상담을 완료하는데 걸리는 기간이 퇴사하는 날을 넘어간다면
    dp[i] = dp[i + 1]     # 해당 날짜는 새로운 상담을 잡지 않음
  else:
    dp[i] = max(dp[i + 1], lst[i][1] + dp[i + lst[i][0]])   # 해당 날짜에 상담을 안하는 경우 vs 해당 날짜에 상담을 하는 경우 비교해서 최댓값 저장

print(dp[0])    # dp[0]에는 무조건 최대값만 담겨있음
