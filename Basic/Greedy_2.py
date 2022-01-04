# 곱하기 혹은 더하기

S = input()

list_S = list(map(int, S))

result = 0

for i in range(len(list_S)):
  if list_S[i] <= 1 or result == 0:
    result += list_S[i]
  else:
    result *= list_S[i]

print(result)
