N = int(input())
lst_A = list(map(int, input().split()))
lst_B = list(map(int, input().split()))

S = 0
for i in range(N):
  S += min(lst_A) * max(lst_B)
  lst_A.remove(min(lst_A))
  lst_B.remove(max(lst_B))

print(S)
