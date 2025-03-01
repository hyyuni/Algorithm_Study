N = int(input())
arr = [[0] * 100 for _ in range(100)]
ans = 0
i , j = 0, 0
for _ in range(N):
    x, y = map(int, input().split())
    
    for i in range(10):
        for j in range(10):
            if arr[i+x][j+y] != 1:
                arr[i+x][j+y] = 1

for i in range(100):
    ans += sum(arr[i])

print(ans)