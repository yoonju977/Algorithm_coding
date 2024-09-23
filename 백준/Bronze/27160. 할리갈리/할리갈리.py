def should_ring_bell(cards):
    # 과일의 개수를 저장할 딕셔너리 초기화
    fruit_counts = {
        "STRAWBERRY": 0,
        "BANANA": 0,
        "LIME": 0,
        "PLUM": 0
    }
    
    # 카드를 읽어서 과일의 개수를 합산
    for card in cards:
        fruit, count = card
        fruit_counts[fruit] += count
    
    # 어떤 과일의 개수가 정확히 5개인지 확인
    for count in fruit_counts.values():
        if count == 5:
            return "YES"
    
    return "NO"

# 입력 처리
N = int(input().strip())
cards = []
for _ in range(N):
    S, X = input().strip().split()
    X = int(X)
    cards.append((S, X))

# 결과 출력
print(should_ring_bell(cards))
