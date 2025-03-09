# 📄 5215_햄버거 다이어트
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT

## 1. 설계시 이슈
### [1] 그리디 or 완탐
(맛 / 칼로리) 비율을 계산하여, 해당 비율이 높은 순대로 더하려고 하였다.  
하지만 이런 그리디한 접근방식이 맞진 않았다.  
해당 비율로 계산했을 때 꼭 최적해를 구할 수 있다고 보장할 순 없기 때문이다.  
#### 수정 전 코드 (그리디)
```
    for i in range(N):
        T, K = map(int, input().split())
        food.append((T / K, T, K))

    total = 0
    food.sort(reverse=True)
    for percent, t, k in food:
        if total + k > L:
            continue 
        total += t
        
    print(f"#{test_case} {total}")
```

예를 들어 아래와 같이 세가지 음식이 있을 때를 가정해보자.
```
1) 맛 80, 칼로리 40 -> (비율 2)
2) 맛 100, 칼로리 60 -> (비율 5/3)
3) 맛 50, 칼로리 30 -> (비율 5/3) 
```

**제한 칼로리가 90일 때**
- 비율 순대로 조합을 뽑는 경우:  
1번 선택되고 끝난다.   
80점.

- 실제 정답:  
2,3번 조합이 점수가 더 높다.   
150점.


>따라서 **완전탐색**으로 모든 경우의 수를 따져봐야 한다.  
이 때 itertools의 combination을 사용하여 모든 케이스마다 실행할 수 있겠지만  
백트래킹을 하기 위해 **dfs**로 구현하였다.