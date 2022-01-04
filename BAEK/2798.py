N, M = map(int, input().split())

card_list = list(map(int, input().split()))

sum0, answer = 0, 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum0 = card_list[i] + card_list[j] + card_list[k]
            if (sum0 <= M) and (sum0 > answer):
                answer = sum0

print(answer)
