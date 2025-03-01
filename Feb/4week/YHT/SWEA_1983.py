# T = int(input())  # 테스트 케이스 수
# sco = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

# for i in range(1, T + 1):
#     N, M = map(int, input().split())  # N: 학생 수, M: 학점을 알고 싶은 학생 번호
#     d = []
    
#     # 학생들의 점수를 입력받고 총점 계산
#     for x in range(N):
#         a, b, c = map(int, input().split())
#         total_score = 0.35 * a + 0.45 * b + 0.2 * c
#         d.append((total_score, x))  # (총점, 학생 번호) 형태로 저장
    
#     # 총점 내림차순으로 정렬
#     d.sort(reverse=True, key=lambda x: x[0])
    
#     # N/10명씩 동일한 평점을 부여
#     k = N // 10
#     result = [''] * N  # 각 학생의 학점을 저장할 리스트
    
#     # 각 학생에게 학점 부여
#     for i in range(10):
#         for w in range(k):
#             student_index = d[i * k + w][1]  # 학생 번호로 인덱스 계산
#             result[student_index] = sco[i]  # 해당 학생에게 학점 부여
    
#     # M번째 학생의 학점을 출력
#     print(f"#{i} {result[M - 1]}")
