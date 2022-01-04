from collections import deque

def BFS():    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))
        
    
    
M, N = map(int, input().split())

box = []
queue = deque()

for i in range(N):
    box.append(list(map(int, input().split())))
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

BFS()
result = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        else:
            result = max(result, box[i][j])
print(result-1)
