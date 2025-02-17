short = [int(input()) for _ in range(9)]
minus = sum(short) - 100

for i in range(9):
    for j in range(i+1,9):
        if short[i]+short[j] == minus:
            a = short[i]
            b = short[j]

short.remove(a)
short.remove(b)
short.sort()
for s in short:
    print(s)