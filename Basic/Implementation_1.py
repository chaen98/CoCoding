# 상하좌우

# method 1 #
N = int(input())
MOVE = list(map(str, input().split()))

result_x = 0
result_y = 0

start = False

for m in MOVE:
    if m == 'L':
        result_x -= 0 if result_x == 0 else 1
    elif m == 'R':
        result_x += 0 if start == True and result_x == N - 1 else 1
    elif m == 'U':
        result_y -= 0 if result_y == 0 else 1
    elif m == 'D':
        result_y += 0 if start == True and result_y == N - 1 else 1
    
    start = True
    
print(result_y + 1, result_x + 1)





# method 2 #
N = int(input())
MOVE = list(map(str, input().split()))

x = 0
y = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for m in MOVE:
  for i in range(len(move_type)):
    if m == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    
  if nx < 0 or nx > N or ny < 0 or ny > N:
    continue

  x = nx
  y = ny

print(x+1, y+1)
