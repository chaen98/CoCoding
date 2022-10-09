def Check(k, y, x):
    global like
    global zero

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if room[ny][nx] == 0:
                zero += 1
            elif room[ny][nx] in students[k][1:]:
                like += 1


N = int(input())
students = [list(map(int, input().split())) for _ in range(N * N)]
room = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

room[1][1] = students[0][0]
for i in range(1, N**2):  # 학생 순서대로
    sit = [-1, -1]
    max_like, max_zero = -1, -1

    for j in range(N):  # 교실의 자리를 하나씩 확인
        for k in range(N):
            like, zero = 0, 0

            if room[j][k] == 0:  # 비어있는 자리라면
                Check(i, j, k)  # 인접한 4군데 자리 확인

                if like > max_like:  # 조건 1
                    sit = [j, k]
                    max_like = like
                    max_zero = zero
                elif like == max_like:  # 조건 2
                    if zero > max_zero:
                        sit = [j, k]
                        max_like = like
                        max_zero = zero
                elif like == max_like and zero == max_zero:
                    if j < sit[0]:  # 조건 3-1
                        sit = [j, k]
                        max_like = like
                        max_zero = zero
                    elif j == sit[0] and k < sit[1]:  # 조건 4
                        sit = [j, k]
                        max_like = like
                        max_zero = zero

    room[sit[0]][sit[1]] = students[i][0]  # 조건에 맞게 자리 확정

students.sort()  # 만족도 계산을 위해 입력받은 학생 번호를 번호 순대로 정렬

result = 0
for r in range(N):  # 교실의 자리를 차례로 돌며 만족도 조사
    for c in range(N):
        score = 0
        num = room[r][c]

        for i in range(4):  # 인접한 자리에 좋아하는 학생이 있는지 확인
            nx = c + dx[i]
            ny = r + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if room[ny][nx] in students[num - 1][1:]:
                    score += 1

        if score == 1:
            result += 1
        elif score == 2:
            result += 10
        elif score == 3:
            result += 100
        elif score == 4:
            result += 1000

print(result)
