N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key = lambda x:(x[1], x[0]))

end_time = data[0][1]
result = 1
for i in range(1, N):
  if data[i][0] >= end_time:
    end_time = data[i][1]
    result += 1

print(result)
