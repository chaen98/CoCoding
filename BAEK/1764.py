### 2중 for문 -> 시간초과
N , M = map(int, input().split())

lst_N = [input() for _ in range(N)]
lst_M = [input() for _ in range(M)]

result = []
for i in range(N):
  for j in range(M):
      if lst_N[i] == lst_M[j]:
        result.append(lst_N[i])

result.sort()

print(len(result))
for r in result:
  print(r)



### 사전 자료형 Counter 라이브러리 사용 -> 통과(메모리는 크나 시간 더 짧음)
from collections import Counter

N , M = map(int, input().split())

lst = [input() for _ in range(N+M)]

result = []
mode = Counter(lst).most_common()

for i in range(len(mode)):
  if mode[i][1] == 2:
    result.append(mode[i][0])

result.sort()

print(len(result))
for r in result:
  print(r)



### 교집합 사용 -> 통과(메모리는 더 작으나 시간 더 오래걸림)
N , M = map(int, input().split())

lst_N = [input() for _ in range(N)]
lst_M = [input() for _ in range(M)]

intersection = list(set(lst_N) & set(lst_M))
intersection.sort()

print(len(intersection))
for i in intersection:
  print(i)
