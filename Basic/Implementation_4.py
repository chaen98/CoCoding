# 문자열 재정렬

S = list(input())

result = []
x = 0

for s in S:
  if s.isalpha():       # 알파벳인지 확인 / 숫자인지 확인: num.isdigit()
    result.append(s)

  else:
    x += int(s)

result.sort()

if x != 0:
  result.append(str(x))

print(''.join(result))      # 모든 요소를 합쳐 하나로 반환(공백없음) / ' '.join(result) -> 공백있음
