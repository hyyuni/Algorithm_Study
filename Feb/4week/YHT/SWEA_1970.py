T = int(input())
for i in range(1, T + 1):
    a = int(input())
    b = c = d = e = f = g = k=h = 0
    
    while a >= 10:
        if a >= 50000:
            b += a // 50000
            a %= 50000
        elif a >= 10000:
            c += a // 10000
            a %= 10000
        elif a >= 5000:
            d += a // 5000
            a %= 5000
        elif a >= 1000:
            e += a // 1000
            a %= 1000
        elif a >= 500:
            f += a // 500
            a %= 500
        elif a >= 100:
            g += a // 100
            a %= 100
        elif a >= 50:
            h += a // 50
            a %= 50
       	elif a>=10:
            k=a//10
            a%=10

    print(f'#{i}') 
    print(b,c,d,e,f,g,h,k)
