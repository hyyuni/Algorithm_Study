# 조교의 성적 매기기
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # 공백을 기준으로 N과 K 분리
    
    grade = [] # 총점 저장할 리스트 선언

    for i in range(N): # N개 만큼 입력 받기
        mid, final, hw = map(int, input().split()) # 공백을 기준으로 점수 분리
        total = mid * 0.35 + final * 0.45 + hw * 0.2 # 학생 당 총점
        grade.append((total, i)) # grade에 총점과 학생 번호 튜플로 추가
 
    grade.sort(reverse=True) # 점수 내림차순 정렬
    
    rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0'] # 등급 리스트
    grade_person= N //10 # 등급 당 할당할 인원 수 

    # 등급 부여 
    student_rank = {} # 학생 등급 딕셔너리 선언
    for i in range(N):
        student_rank[grade[i][1]] = rank[i//grade_person] # i번 학생에게 등급 부여
    
    print(f'#{tc} {student_rank[K-1]}') # K의 등급 출력
    