from itertools import combinations

L, C = map(int, input().split())
lst = list(map(str, input().split()))

comb = list(combinations(lst, L))
data = []
for c in comb:
  consonants, vowels = 0, 0   # 자음 모음 갯수 카운트
  for i in range(L):
    if c[i] == 'a' or c[i] == 'e' or c[i] == 'i' or c[i] == 'o' or c[i] == 'u':
      vowels += 1
    else:
      consonants += 1

  if consonants > 1 and vowels > 0:   # 최소 2개 이상의 자음 & 최소 1개 이상의 모음일 때
    result = ''.join(sorted(list(c)))   # 조합을 정렬해서 str 형태로 result에 저장
    data.append(result)

data.sort()   # 데이터들을 다시 사전순으로 정렬
for d in data:
  print(d)
