import math

def isPrime(x):   # 소수 판별 함수
  if x == 1:
    return False
  elif x == 2:
    return True
  else:
    for i in range(2, int(math.sqrt(x)) + 1):     # x를 2부터 루트x까지의 숫자로 나누었을 때, 0이 될 수 있다면 소수가 아님
      if (x % i) == 0:
        return False
    return True



N = int(input())    # 1 <= N <= 1,000,000

for n in range(N, 1003002):   # 범위 설정: 주어진 N이 1,000,000 일때, N보다 크거나 같고 소수이면서 펠린드롬인 수는 1003001이기 때문에
  new = n
  lst = list(map(str, str(n)))    # int형 new 변수를 한자리씩 떼어 lst에 저장
  if len(lst) == 1:               # 한자리 수일 경우는 모두 펠린드롬이기 때문에 소수 검사만 실행
    if isPrime(new):              # isPrime이 True일 경우, N보다 크거나 같은 가장 작은 소수를 찾은 것
      break

  elif len(lst) == 2 or len(lst) == 3:    # 두~세자리일 경우는 첫번째 숫자와 마지막 숫자가 일치해야 함
    if lst[0] == lst[-1]:                 # 펠린드롬일 경우 소수 판별
      if isPrime(new):
        break

  elif len(lst) == 4 or len(lst) == 5:            # 네~다섯자리일 경우는 첫번째와 마지막 숫자 일치 & 두번째와 끝에서 두번째 숫자 일치해야 함
    if lst[0] == lst[-1] and lst[1] == lst[-2]:   # 펠린드롬일 경우 소수 판별
      if isPrime(new):
        break

  elif len(lst) == 6 or len(lst) == 7:
    if lst[0] == lst[-1] and lst[1] == lst[-2] and lst[2] == lst[-3]:
      if isPrime(new):
        break

print(new)
