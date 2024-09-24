import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n은 표의 크기, m은 구간 합을 구하는 횟수

# 배열 A는 주어진 표의 값들을 저장하는 배열, 1-based index로 사용{(0,0)의 더미 채우기)
A = [[0] * (n + 1)]  # 첫 번째 행을 0으로 채운 더미 데이터로 시작
D = [[0] * (n + 1) for _ in range(n + 1)]  # 누적 합 배열

# 표 A 입력 받기
for i in range(n):
    A_row = [0] + list(map(int, input().split()))  # 각 행을 1-based index로 저장
    A.append(A_row)

# 2차원 누적 합 배열 D 채우기(0,0)의 경우 어차피 빠지니까 제외 다만 넣고 싶다면 계산해서 넣어주면 됨
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

# 구간 합 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)