# 음료수 얼려먹기

def DFS(x, y):
  if x < 0 or x >= N or y < 0 or y >= M:
    return False

  if box[x][y] == 0:
    box[x][y] = 1
    
    DFS(x-1, y)
    DFS(x+1, y)
    DFS(x, y-1)
    DFS(x, y+1)
    return True

  return False


N, M = map(int, input().split())

box = []
for i in range(N):
  box.append(list(map(int, input())))
  
result = 0

for i in range(N):
  for j in range(M):
      if DFS(i, j) == True:
        result += 1

print(result)
