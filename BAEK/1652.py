N = int(input())

room = [[] for _ in range(N)]
for i in range(N):
  tmp = input()
  room[i] = list(tmp)


cnt_w, cnt_h = 0, 0

for i in range(N):
  for j in range(N-1):
    if room[i][j] == room[i][j+1] and room[i][j] == '.':
      cnt_w += 1
      if j > 0:
        if room[i][j] == room[i][j-1]:
          cnt_w -= 1

for i in range(N):
  for j in range(N-1):
    if room[j][i] == room[j+1][i] and room[j][i] == '.':
      cnt_h += 1
      if j > 0:
        if room[j][i] == room[j-1][i]:
          cnt_h -= 1

print(cnt_w, cnt_h, sep=' ')



# ..XX.. 인 경우 2가지 방법이 되기 때문에 이 부분을 생각하는 것이 main point.
