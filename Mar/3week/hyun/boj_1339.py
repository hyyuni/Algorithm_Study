N = int(input())

dic = {}
lst = []
ans = 0
for _ in range(N):
    alphabets = input()
    for i in range(len(alphabets)):
        if alphabets[i] not in dic: # dictionary의 value에 자릿수 채우기
            dic[alphabets[i]] = 10**(len(alphabets)-i-1)
        else: # 이미 있다면 해당 위치에 자릿수와 빈도수 더해주기 111 -> 222
            dic[alphabets[i]] = dic[alphabets[i]] + 10**(len(alphabets)-i-1)

# 내림차순 정렬하고 제일 많은 자릿수+빈도수를 가진 단어부터 9,8,7,6,.. 곱하기
lst = sorted(dic.values(), reverse=True)

for i in range(len(lst)):
    ans += (9-i)*lst[i]

print(ans)