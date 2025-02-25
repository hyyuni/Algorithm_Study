# 초심자의 회문 검사
T = int(input())

for tc in range(1, T+1):
    word = list(map(str, input().strip()))

    for i in range(len(word)):
        if word[0] == word[-1]:
            ans =1
        else:
            ans = 0

    print(f'#{tc} {ans}')