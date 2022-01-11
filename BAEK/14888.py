from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))      # 숫자
data = list(map(int, input().split()))      # 연산자 갯수
operators = []         # 연산자 갯수별로 리스트에 저장
for i in range(4):
  if i == 0:      # data[0]에는 +의 갯수 저장되어 있으므로
    for j in range(data[0]):    # +의 갯수 만큼 리스트에 저장
      operators.append('+')
  elif i == 1:
    for j in range(data[1]):
      operators.append('-')
  elif i == 2:
    for j in range(data[2]):
      operators.append('*')
  else:
    for j in range(data[3]):
      operators.append('/')

permu = list(set(permutations(operators, N-1)))     # 연산자로 만들 수 있는 모든 순열 저장(단, 같은 연산자가 여러 개 있을 경우 중복되므로 set함수를 통해 중복되는 것 제거)

results = []
for p in permu:       # 백트래킹: 모든 순열 체크
  calculate = nums[0]

  for k in range(N-1):   # 숫자 갯수만큼 연산
    if p[k] == '+':
      calculate += nums[k+1]
    elif p[k] == '-':
      calculate -= nums[k+1]
    elif p[k] == '*':
      calculate *= nums[k+1]
    else:                     # 나눗셈: 음수를 양수로 나눌 경우를 고려
      if calculate < 0:
        calculate = abs(calculate) // nums[k+1]   # 양수로 바꾼 뒤 몫을 계산하고 다시 음수로 변경
        calculate = -calculate
      else:
        calculate //= nums[k+1]

  results.append(calculate)   # 결과 리스트에 저장


print(max(results), min(results), sep='\n')
