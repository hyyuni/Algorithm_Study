# 단어 수학
# https://www.acmicpc.net/problem/1339

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("boj_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

from collections import defaultdict

N = int(input())

info = defaultdict(int)
digit_size = 0
word_li = []
for _ in range(N):
    word = input().strip()

    size = 0
    for i in range(len(word)-1, -1, -1):
        w = word[i]
        info[w] += 10 ** size
        size += 1

info_keys = []
for key, val in info.items():
    info_keys.append((val, key))
info_keys.sort(reverse=True)

num = 9
answer = 0
for val, ap in info_keys:
    answer += (val * num)
    num -= 1

print(answer)