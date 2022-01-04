N = int(input())

bcheck = False

N_list = []
for x in range(1, N+1):
    N_list = list(map(int, str(x)))
    result = x + sum(N_list)
    if result == N:
        bcheck = True
        print(x)
        break

if bcheck == False:
    print(0)
