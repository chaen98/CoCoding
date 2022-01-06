from itertools import permutations    # 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열

N = int(input())
A = list(map(int, input().split()))
data = list(permutations(A, N))     # 모든 순열을 data에 리스트로 저장

lst = []
for i in range(len(data)):      # 모든 경우의 수를 모두 계산
  result = 0
  for j in range(N-1): 
    result += abs(data[i][j] - data[i][j+1])

  lst.append(result)

print(max(lst))     # 그 중 최대값만



# 최대 8개의 정수로 이루어져 있기 때문에 최대 8! = 40320 경우의 수임
# 따라서 모든 경우의 수를 계산해도 시간초과가 없음
