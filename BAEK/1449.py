N, L = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

result = 1
start = lst[0]
for i in range(1, N):
  result += 1
  if lst[i] - start < L:
    result -= 1
  else:
    start = lst[i]

print(result)
