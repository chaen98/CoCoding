N, K = map(int, input().split())
belt = list(map(int, input().split()))

robot = [False] * N     # 로봇이 존재하는 곳 = True
answer = 0


while True:
  answer += 1

  belt.insert(0, belt.pop(-1))      # 마지막 위치의 벨트를 맨 앞으로 옮겨 회전
  robot.insert(0, robot.pop(-1))
  robot[-1] = False     # 내리는 위치에 로봇이 존재한다면 바로 내리기

  for i in range(N-2, 0, -1):
    if robot[i] == True and robot[i+1] == False and belt[i+1] > 0:      # 현재 위치에 로봇이 존재하고 다음 칸에 로봇이 없으며 내구도가 0보다 큰 경우에만 다음 칸으로 로봇 이동시키기
      robot[i] = False
      robot[i+1] = True
      belt[i+1] -= 1      # 내구도 1 감소

  robot[-1] = False     # 내리는 위치에 로봇이 존재한다면 바로 내리기

  if belt[0] > 0:     # 올리는 위치의 내구도가 0보다 크다면 로봇 올리기
    robot[0] = True
    belt[0] -= 1      # 내구도 1 감소


  if belt.count(0) >= K:      # 내구도가 0인 칸의 개수가 K보다 크다면 종료
    print(answer)
    break
