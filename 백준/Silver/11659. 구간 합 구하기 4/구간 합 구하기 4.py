import sys
input = sys.stdin.read # 전체 입력을 한 번에 처리

def main():
    data = input().split()
    
    N = int(data[0]) 
    M = int(data[1]) 
    
    numbers = list(map(int, data[2:N+2]))  
    queries = data[N+2:] 
    
    # 누적 합 배열 생성
    prefix_sum = [0] * (N + 1)
    
    # 누적 합 계산
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]
    
    result = []
    
    # 각 구간에 대한 결과 계산
    for idx in range(M):
        i = int(queries[2 * idx])
        j = int(queries[2 * idx + 1])
        result.append(str(prefix_sum[j] - prefix_sum[i - 1]))
    
    sys.stdout.write("\n".join(result) + "\n")
    
main()