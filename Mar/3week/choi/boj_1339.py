N = int(input())

words = [list(map(str, input().strip())) for _ in range(N)]
dict = {}
for word in words:
    for i in range(len(word)):
        wor = word[i]
        if wor in dict:
            dict[wor] += 10**(len(word) - i -  1)
        else:
            dict[wor] = 10**(len(word) - i -  1)

abc = sorted(dict.items(), key=lambda x: x[1], reverse=True)

res = 0 
for i in range(len(abc)):
    _, value = abc[i]
    res += value * (9-i)
print(res)