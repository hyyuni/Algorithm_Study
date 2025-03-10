N, K = map(int, input().split())
words = [list(input()) for _ in range(N)]
alp = [0] * 26
search_word = set()
ans = 0
for i in ['a', 'n', 't', 'i', 'c']:
    alp[ord(i) - ord('a')] = 1
if K < 5:
    print(0)
    exit()
if K >= 26:
    print(N)
    exit()

for word in words:
    for alpa in word:
        if alp[ord(alpa) - ord('a')] == 0:
            search_word.add(ord(alpa) - ord('a'))
search_word = list(search_word)


def dfs(index, cnt):
    global ans
    if cnt == K-5:
        count_read = 0
        for word in words:
            flag = 0
            for alpa in word:
                if alp[ord(alpa) - ord('a')] == 0:
                    flag = 1
                    break
            if flag == 0:
                count_read += 1
        ans = max(ans, count_read)
        return
        

    for i in range(index, len(search_word)):
        alp[search_word[i]] = 1
        dfs(i+1, cnt+1)
        alp[search_word[i]] = 0
dfs(0,0)
print(ans)