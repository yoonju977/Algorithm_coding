#내가 짠 코드
import sys
from collections import defaultdict

# 입력 받기
n, m = map(int, input().split())  # N과 M 입력
arr = list(map(int, input().split()))  # N개의 수 입력

# 누적합 배열을 M으로 나눈 나머지들의 개수를 저장하는 딕셔너리
prefix_mod = defaultdict(int)

# 누적합과 결과 개수 초기화
prefix_sum = 0
result = 0

# 처음 나머지가 0인 경우도 카운트 (구간이 처음부터 끝까지일 때 나누어 떨어짐)
prefix_mod[0] = 1  # 누적합이 0일 때 카운트를 먼저 추가

# 누적합 계산 시작
for i in range(n):
    prefix_sum += arr[i]
    
    # 누적합을 M으로 나눈 나머지를 구함 (음수 방지)
    mod = prefix_sum % m
    
    # 동일한 나머지가 존재하면, 그 구간들은 나누어떨어지는 구간을 형성함
    result += prefix_mod[mod]
    
    # 현재 누적합 나머지의 개수를 증가시킴
    prefix_mod[mod] += 1

# 결과 출력 (나누어 떨어지는 구간의 개수)
print(result)
