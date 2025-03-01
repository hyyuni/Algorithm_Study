# 카이사르 암호
arr = list(map(ord, input()))

for i in range(len(arr)):
    if (64 < arr[i] and arr[i] < 68) or (96 < arr[i] and arr[i] < 100):
        arr[i] = arr[i] + 26
    arr[i] = arr[i] - 3
    print(chr(arr[i]), end = '')

# ord(char -> int(ascii) chr(int) -> character