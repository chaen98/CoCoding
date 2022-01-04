from collections import Counter

N = int(input())
list0 = [int(input()) for _ in range(N)]
list0.sort()

print(round(sum(list0)/N))    # 산술평균
print(list0[(N//2)])    # 중앙값

# 최빈값
most = Counter(list0).most_common(2)
if len(list0) > 1:
  if most[0][1] == most[1][1]:
    print(most[1][0])
  else:
    print(most[0][0])
else:
  print(most[0][0])


print(max(list0) - min(list0))    #범위
