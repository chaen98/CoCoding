N = int(input())

num = [0, 0]
if N // 10 == 0:
  num[1] = N
else:
  num[0] = N // 10
  num[1] = N % 10

new = 0
cnt = 0

while True:
  tmp = (num[0] + num[1]) % 10
  new = (num[1] * 10) + tmp

  num[0] = new // 10
  num[1] = new % 10
  
  cnt += 1
  
  if new == N:
    break


print(cnt)
