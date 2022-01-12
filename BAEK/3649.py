import sys

while True:
  try:
    x = int(input()) * 10000000
    n = int(input())
    lego = [int(sys.stdin.readline()) for _ in range(n)]
    lego.sort()

    small_val, large_val = 0, n-1
    no_ans = True

    while small_val < large_val:
      if lego[small_val] + lego[large_val] == x:
        print('yes', lego[small_val], lego[large_val])
        no_ans = False
        break

      elif lego[small_val] + lego[large_val] < x:
        small_val += 1

      else:   # lego[small_val] + lego[large_val] > x
        large_val -= 1
    
    if no_ans:
      print('danger')

  except:
    break



# 조합으로 푸는 것을 시도했지만 메모리 초과 발생함
# 합이 구멍의 크기보다 작다면 합을 크게 만들기 위해 작은 인덱스 +1
# 합이 구멍의 크기보다 크다면 합을 작게 만들기 위해 큰 인덱스 -1

# 테스트 케이스가 여러 개이며 몇 개를 입력받을지 모르기 때문에 try/except 구문 사용
