from collections import Counter

card, nums = [], []
for _ in range(5):
  a, b = map(str, input().split())
  card.append([a, int(b)])
  nums.append(int(b))

card.sort(key = lambda x:x[1])
# print(f'card: {card} \n')

score = 0
bcheck = False

# 색이 같은 경우
if card[0][0] == card[1][0] and card[0][0] == card[2][0] and card[0][0] == card[3][0] and card[0][0] == card[4][0]:
  for i in range(4):
    if card[i+1][1] == card[i][1] + 1:
      bcheck = True
    else:
      bcheck = False
      break
  
  if bcheck == True:    # 규칙 1. 색이 같음 & 숫자가 연속적
    score = 900 + card[4][1]
  else:                 # 규칙 4. 색만 같은 경우
    score = 600 + card[4][1]

  
# 색이 다른 경우
else:
  mode = Counter(nums).most_common(2)    # 같은 숫자의 갯수를 파악하기 위함
  # print(f'mode: {mode} \n')

  for i in range(4):
    if card[i+1][1] == card[i][1] + 1:
      bcheck = True
    else:
      bcheck = False
      break
  
  if bcheck == True:    # 규칙 5. 숫자가 연속적
    score = 500 + card[4][1]
  elif mode[0][1] == 4:
    score = 800 + mode[0][0]    # 규칙 2. 4장의 숫자 동일
  elif mode[0][1] == 3:
    if mode[1][1] == 2:
      score =  700 + (mode[0][0] * 10) + mode[1][0]   # 규칙 3. 3장의 숫자 동일 & 2장의 솟자 동일
    else:
      score = 400 + mode[0][0]    # 규칙 6. 3장의 숫자 동일
  elif mode[0][1] == 2:
    if mode[1][1] == 2:    # 규칙 7. 2장의 숫자 동일 & 2장의 숫자 동일
      if mode[0][0] > mode[1][0]:
        score = 300 + (mode[0][0] * 10) + mode[1][0]
      else:
        score = 300 + (mode[1][0] * 10) + mode[0][0]
    else:
      score = 200 + mode[0][0]    # 규칙 8. 2장의 숫자 동일
  else:
    score = 100 + card[4][1]    # 규칙 9. 어떤 경우도 해당x


print(score)
