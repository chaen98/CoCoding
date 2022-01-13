def Backtracking(x):
  for i in range(1, (x//2) + 1):    # 수열 길이의 절반만큼 확인하면 모두 검사 가능
    if result[-i:] == result[-(i*2):-i]:    # 이전 부분 수열과 동일한 것이 있다면 False 리턴하도록
      return False
  
  if x == N:
    return True

  for n in number:    # 1부터 3까지 하나씩 붙여가며 좋은 수열인지 판단 & 가장 작은 수를 구해야 하므로 1부터 붙여보기
    result.append(n)
    if Backtracking(len(result)):   # True를 리턴한다면, 좋은 수열 + 길이 N을 만족한 것임
      print(''.join(list(result)))
      exit(0)
    del result[-1]    # 좋은 수열이 아니므로 마지막 원소 다시 지워줌



N = int(input())

number = ['1', '2', '3']
result = ['1']      # 첫 번째 수는 무조건 1
Backtracking(1)
