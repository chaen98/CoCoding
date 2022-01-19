N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = N    # 총감독관은 무조건 1명씩 배정되어야 하므로 시험장 갯수만큼 더하고 시작
for a in A:   # 시험장 마다 몇명의 부감독관이 추가로 필요한지 확인
  people = a - B    # 남은 응시생 - 총감독관이 감시할 수 있는 응시자 수
  if people > 0:      # 남은 응시생이 0명 보다 많을 경우 부감독관 추가
    result += (people // C)

    if (people % C) != 0:
      result += 1

print(result)
