import sys

T = int(input())

for _ in range(T):
  N = int(input())
  data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

  data.sort()       # 서류심사 성적 순으로 정렬
  minimum = data[0][1]    # 서류심사 1등의 면접 성적 저장
  result = 0
  for d in data:
    if d[1] <= minimum:   # 서류 심사 성적이 낮기 때문에 면접 성적이 더 높은 사람만 선발
      result += 1
      minimum = min(minimum, d[1])    # 가장 높은 면접 성적으로 업데이트(다음 지원자는 서류 성적이 더 낮기 때문에 가장 높은 면접 성적보다 더 높아야 선발 가능)

  print(result)


# 7번 시도했지만 시간초과&실패
# 해결방법 찾아봄
