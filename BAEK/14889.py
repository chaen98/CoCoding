from itertools import combinations
from itertools import permutations

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
person = [i for i in range(N)]              # N명을 구분하기 위해 번호 부여

comb = list(combinations(person, N//2))     # 조합: 팀을 나눌 수 있는 가짓수. 만약 20가지라면 앞의 10가지와 뒤에서부터 10가지는 같은 경우임.
start = comb[:len(comb)//2]                 # 스타트 팀 배정
link = comb[(len(comb)//2):]                # 링크 팀 배정
link.reverse()                              # 뒤에서부터 10가지이기 때문에 리스트의 순서 반대로

start_score = []                            # 각 조합별로 스타트 팀의 능력치 저장
for s in start:                             # 모든 조합의 능력치를 계산하도록
  result = 0
  data = list(permutations(s, 2))           # 순열: 팀의 능력치는 팀에 속한 모든 쌍의 능력치 이므로 순열을 이용해 데이터 2개씩 추출

  for d in data:                            # 모든 쌍의 능력치 계산하도록
    result += lst[d[0]][d[1]]               # 능력치를 모두 합하여 start_score에 최종적으로 저장되도록

  start_score.append(result)

link_score = []                             # 링크 팀도 마찬가지로 계산
for l in link:
  result = 0
  data = list(permutations(l, 2))

  for d in data:
    result += lst[d[0]][d[1]]

  link_score.append(result)

power = []                                 # 스타트 팀과 링크 팀의 능력치 차이를 저장
for i in range(len(start_score)):
  power.append(abs(start_score[i] - link_score[i]))     # 가장 작은 차이를 출력할 수 있도록 모든 능력치 차이를 절댓값으로 저장

  
print(min(power))
