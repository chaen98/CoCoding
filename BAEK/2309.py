lst = [int(input()) for _ in range(9)]


for i in range(8):
  for j in range(i+1, 9):
    if sum(lst) - lst[i] - lst[j] == 100:
      remove_1 = lst[i]     # lst.remove(lst[i]) 로 할 경우, 실행되는 순간 i+1번 이후 원소들이 전부 한 칸 씩 앞으로 당겨져 리스트의 크기가 줄어들고, 아랫줄은 범위를 벗어났기 때문에 실행할 수 없음.
      remove_2 = lst[j]
      break

lst.sort()
for k in range(9):
  if lst[k] == remove_1 or lst[k] == remove_2:
    continue
  else:  
    print(lst[k])
