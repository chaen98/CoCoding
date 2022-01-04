# 왕실의 나이트

pos = str(input())

pos = list(pos)

nx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ny = ['1', '2', '3', '4', '5', '6', '7', '8']

for i in range(len(nx)):
  if pos[0] == nx[i]:
    x = i
    break

for j in range(len(ny)):
  if pos[1] == ny[j]:
    y = j
    break

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

count = 0

for k in range(8):
  result_x = x + dx[k]
  result_y = y + dy[k]

  if result_x < 0 or result_y < 0 or result_x > 7 or result_y > 7:
    continue

  count += 1

print(count)
