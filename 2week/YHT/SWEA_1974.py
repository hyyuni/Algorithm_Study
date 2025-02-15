T = int(input())

for t in range(1, T + 1):
    N = int(input())
    result = ""
    
    for _ in range(N):
        C, K = input().split()
        result += C * int(K)
    
    print(f"#{t}")
    
    for i in range(0, len(result), 10):
        print(result[i:i+10])