# i번 세로선 결과가 i번인지 확인
def Move():
  # 모든 세로선 검사
  for n in range(N):
    tmp = n
    for h in range(H):
      if ladder[h][tmp]:    # 가로선 있으면 이동
        tmp += 1
      elif ladder[h][tmp-1]:
        tmp -= 1

    if n != tmp:    # 결과가 같지 않으면 false
      return False    
  return True



# DFS로 Backtracking 수행
def DFS(x, y, cnt):
  global ans
  # i번 세로선 결과가 i번이면 종료
  if Move():
    ans = min(ans, cnt)
    return
  # 카운트 값이 3이 되거나(다음 DFS 수행 후 가로선 개수가 4가 되기 때문), 이전 결과값보다 커지면(최소한의 가로선을 출력해야 하기 때문) 종료
  if cnt == 3 or ans <= cnt:
    return

  
  for i in range(x, H):
    k = y if i == x else 0
    for j in range(k, N-1):
      if not ladder[i][j] and not ladder[i][j+1] and not ladder[i][j-1]:      # 해당 지점에 가로선 그었을 때, 연속되지 않는 경우에만
        ladder[i][j] = True    # 가로선 추가
        DFS(i, j+2, cnt+1)    # 가로선 연속되지 않도록 2증가
        ladder[i][j] = False    # 백트래킹



N, M, H = map(int, input().split())
ladder = [[False] * N for _ in range(H)]

if M == 0:
  print(0)
else:
  for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = True

  ans = 4
  DFS(0, 0, 0)
  print(ans if ans < 4 else -1)




# 다른 코드 풀이 참고해서 구현함
# 완벽한 이해 X (다시 봐야함)
