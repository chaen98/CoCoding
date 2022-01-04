# 1이 될 때 까지

# method 1 #
N, K = map(int, input().split())

result = 0

if N < K:
    result = N - 1

elif N == K:
    result = 1

else:
    while N != 1:
        if (N % K) == 0:
            N = N / K
        else:
            N -= 1
            
        result += 1

print(result)



# method 2 #
N, K = map(int, input().split())

result = 0

while True:
  # K로 나눠질 때까지 뺄셈
  target = (N // K) * K
  result += (N - target)
  N = target

  if N < K:
    break

  result += 1
  N //= K

result += (N - 1)
print(result)
