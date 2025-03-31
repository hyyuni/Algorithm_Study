# 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t) // w  # 증가/감소 확인
b = (q + t) // h  # 증가/감소 확인

if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)