N, K = map(int, input().split())     # 멀티탭 구멍 갯수, 전기용품 총 사용 횟수
product = list(map(int, input().split()))    # 전기용품 사용 순서
standby = product.copy()      # 앞으로 사용해야 하는 대기열
tab = []        # 멀티탭에 꽂혀있는 전기용품 종류

result = 0
for k in range(K):
  if product[k] in tab:     # 멀티탭에 꽂혀있다면
    standby.remove(standby[0])      # 대기열에서 제거

  else:       # 멀티탭에 꽂혀있지 않다면
    if len(tab) < N:      # 멀티탭에 자리가 있다면
      tab.append(product[k])      # 멀티탭에 꽂기
      standby.remove(standby[0])      # 대기열에서 제거

    else:       # 멀티탭에 자리가 없다면
      maximum, item = 0, 0      # 제거할 전기용품 & 전기용품의 인덱스

      for t in tab:
        if t not in standby:    # 멀티탭에 꽂혀있는 t가 더 이상 대기열에 없다면
          item = t      # t를 제거하도록
          break
        else:       # 멀티탭에 꽂혀있는 용품들이 나중에 다시 사용해야 하는 것들이라면
          if standby.index(t) > maximum:      # 더 나중에 사용할 전기용품을 우선적으로 제거하도록
            maximum = standby.index(t)
            item = t

      tab.remove(item)      # 멀티탭에서 제거
      result += 1       # 플러그 뺀 횟수 +1 증가

      tab.append(product[k])      # 멀티탭에 꽂기
      standby.remove(standby[0])      # 대기열에서 제거


print(result)
