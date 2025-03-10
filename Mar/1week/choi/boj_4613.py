alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
quick = input()

while quick != '#':
    result = 0
    for i in range(len(quick)):
        result += alphabet.index(quick[i]) * (i+1)
    print(result)
    quickg = input()