def Rotate(s, d):
  if d == 1:
    tooth[s].insert(0, tooth[s][7])
    del tooth[s][8]

  else:
    tooth[s].append(tooth[s][0])
    tooth[s].remove(tooth[s][0])


tooth = [list(map(int, input())) for _ in range(4)]
tooth.insert(0, [])
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

for i in range(K):
  select = []
  direction = []

  select.append(rotation[i][0])     # 선택한 톱니 저장
  direction.append(rotation[i][1])      # 톱니의 회전 방향 저장

  bRotate = True
  for j in range(rotation[i][0], 4):      # 해당 톱니로부터 오른쪽 방향에 있는 톱니와 극 확인
    if tooth[j][2] != tooth[j+1][6] and bRotate == True:
      select.append(j+1)
      if (j+1) - select[0] == 1 or (j+1) - select[0] == 3:    # 해당 톱니로부터 얼마나 떨어져있는지에 따라 방향 결정
        direction.append(-direction[0])   #바로 옆에 있을 때는 반대방향을 돌기
      else:
        direction.append(direction[0])
    else:
      bRotate = False
      break
    
  bRotate = True
  for k in range(rotation[i][0], 1, -1):      # 해당 톱니로부터 왼쪽 방향에 있는 톱니와 극 확인
    if tooth[k-1][2] != tooth[k][6] and bRotate == True:
      select.append(k-1)
      if select[0] - (k-1) == 1 or select[0] - (k-1) == 3:
        direction.append(-direction[0])
      else:
        direction.append(direction[0])
    else:
      bRotate = False
      break


  for l in range(len(select)):
    Rotate(select[l], direction[l])


result = 0
if tooth[1][0] == 1:
  result += 1
if tooth[2][0] == 1:
  result += 2
if tooth[3][0] == 1:
  result += 4
if tooth[4][0] == 1:
  result += 8

print(result)
