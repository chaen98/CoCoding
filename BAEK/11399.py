N = int(input())
lst = list(map(int, input().split()))

lst.sort()

result = 0
for n in range(N):
  result += lst[n] * (N - n)

print(result)
