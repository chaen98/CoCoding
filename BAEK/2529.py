k = int(input())
lst = list(map(str, input().split()))

maxi = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
mini = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(k):
  for j in range(k):
    if lst[j] == '<':   # 부등호가 < 라면 maxi가 순서열을 만족하지 못하기 때문에 뒷 숫자와 바꿔줌
      if maxi[j] > maxi[j+1]:   # 올바르게 정렬되지 않았을 때만(이전 정렬에서 이미 바뀌었다면 또 바꾸지 않기 위해서)
        maxi[j], maxi[j+1] = maxi[j+1], maxi[j]
    else:               # 부등호가 > 라면 mini가 순서열을 만족하지 못하기 때문에 뒷 숫자와 바꿔줌
      if mini[j] < mini[j+1]:
        mini[j], mini[j+1] = mini[j+1], mini[j]

for j in range(k):    # 마지막에 한 번 더 정렬해줘야 함.(부등호 갯수보다 숫자 갯수가 많기 때문에)
  if lst[j] == '<':
    if maxi[j] > maxi[j+1]:
      maxi[j], maxi[j+1] = maxi[j+1], maxi[j]
  else:
    if mini[j] < mini[j+1]:
      mini[j], mini[j+1] = mini[j+1], mini[j]


result_max = ''
result_min = ''
for l in range(k+1):
  result_max += maxi[l]   # maxi와 mini가 문자열이기 때문에 그냥 더해주면 뒤에 추가됨
  result_min += mini[l]

print(result_max, result_min, sep = '\n')



# 그냥 생각나는 대로 구현함
# 백준 알고리즘 분류에는 브루트포스/백트래킹으로 분류되어 있어 재귀함수를 이용한 풀이가 많은 것 같음
