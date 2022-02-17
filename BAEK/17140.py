from collections import defaultdict    # 키의 개수를 세야할 때 사용(딕셔너리에 키가 있는지 확인하지 않고, 없다면 만들어주고 값을 0으로 세팅)
import itertools


# 한 행 or 한 열 별로 정렬
def Sorting(lst):
  dict_lst = defaultdict(int)    # 디폴트 값이 int인 딕셔너리
  for l in lst:    # lst 리스트 안에서
    if l == 0:    # 0 이라면 pass
      continue
    dict_lst[l] += 1    # 0 이 아닐때, 값 +1 증가

  newlst = []
  for l, c in dict_lst.items():    # key와 value를 모두 돌면서
    newlst.append((l, c))    # 새로운 리스트에 저장

  newlst.sort(key = lambda x: (x[1], x[0]))    # 등장 횟수(value)가 커지는 순으로/ 수(key)가 커지는 순으로 정렬
  newlst = list(itertools.chain(*newlst))    # 2차원 리스트를 1차원 리스트로 변경
  
  return newlst[:100]    # 처음 100개를 제외한 나머지 버리기

  
# R연산
def OperateR(A):
  newA = [[0] * 100 for _ in range(100)]
  for i in range(100):    # 모든 행을 돌면서
    new_row = Sorting(A[i])    # 정렬한 후

    for j in range(len(new_row)):    # 정렬된 리스트의 길이만큼
      newA[i][j] = new_row[j]    # 재배열

  return newA


# C연산
def OperateC(A):
  newA = [[0] * 100 for _ in range(100)]
  for i in range(100):    # 모든 열을 돌면서
    col = []
    for j in range(100):    # 한 줄씩
      col.append(A[j][i])    # col 리스트로 만들고

    new_col = Sorting(col)    # 정렬

    for k in range(len(new_col)):    # 정렬된 리스트의 길이만큼
      newA[k][i] = new_col[k]    # 재배열

  return newA


# 행과 열 길이 비교
def CheckLen(A):
  len_row, len_col = 0, 0    # 행&열 길이 초기화

  for i in range(100):    # 모든 열을 돌면서
    while len_row < 100 and A[len_row][i] != 0:    # 해당 위치에 0이 존재할 경우 다음 열로 넘어가서 다시 행의 길이 세기
      len_row += 1

  for j in range(100):    # 모든 행을 돌면서
    while len_col < 100 and A[j][len_col] != 0:    # 해당 위치에 0이 존재할 경우 다음 행으로 넘어가서 다시 열의 길이 세기
      len_col += 1

  return (len_row, len_col)


r, c, k = map(int, input().split())
r, c = r-1, c-1    # 인덱스가 1부터 시작하기 때문에 1을 뺀 후 다시 저장
A = [[0] * 100 for _ in range(100)]
inputA = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
  for j in range(3):
    A[i][j] = inputA[i][j]


ans= 0
while ans <= 100:    # 100초 까지만 세기
  if A[r][c] == k:    # 원하는 값이 나오면 종료
    break

  row, column = CheckLen(A)    # 행&열의 길이 확인 후
  if row >= column:    # 행의 길이가 더 길면
    A = OperateR(A)    # R연산 수행 후 새로운 A 배열 업데이트
  else:    # 열의 길이가 더 길면
    A = OperateC(A)    # C연산 수행 후 새로운 A 배열 업데이트

  ans += 1    # 시간 업데이트

print(ans if ans <= 100 else -1)    # 100 이하라면 시간 출력/ 100 초과라면 -1 출력




# 못 품
# 참고 코드: https://www.youtube.com/watch?v=uudk_wv6b5E
