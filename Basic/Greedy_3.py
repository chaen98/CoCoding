# 모험가 길드

N = int(input())
list_N = list(map(int, input().split()))

list_N.sort()

result = 0
count = 0

for i in list_N:
  count += 1

  if count >= i:
    result += 1
    count = 0

print(result)
