import sys

t = int(input())
for _ in range(t):
  n = int(input())
  contacts = [sys.stdin.readline().rstrip() for _ in range(n)]    # rstrip()을 붙이지 않으면 str 입력 뒤에 \n이 붙게 됨
  contacts.sort()   # 정렬하면 일관성있는 번호 순 대로 정렬되기 때문에 바로 뒤에 있는 번호만 확인해주면 됨

  check = True
  for i in range(n-1):
    length = len(contacts[i])
    if contacts[i] == contacts[i+1][:length]:   # contacts[i]의 길이가 contacts[i+1]의 길이보다 항상 짧기 때문에 contacts[i]의 길이만큼만 비교
      print('NO')
      check = False
      break
  
  if check:
    print('YES')



# 정렬의 성질 & 12번 line의 코딩방법에 대해 알아둬야함
