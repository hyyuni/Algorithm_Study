# 24
sh, sm, ss = map(int, input().split(":")) # 시간 입력을 :으로 나누어 시, 분, 초 변수에 저장
eh, em, es = map(int, input().split(":"))
# 시간 출력

time = eh*3600+em*60+es - (sh*3600+sm*60+ss) # 전부 초로 변환

if time < 0: #00:00:00 - 23:59:59 형태로 출력되므로
    time += 3600*24 # 24시간 더해주기

h = time//3600
m = (time%3600)//60
s = time%60

print("%02d:%02d:%02d\n" %(h, m, s))



