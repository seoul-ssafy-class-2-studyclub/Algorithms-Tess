'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE

문제이해:
총점 = 중간고사(35%) + 기말고사(45%) + 과제(20%)

중*0.35+ 기*0.45 + 과*.20
10개의 평점을 총점이 높은 순서대로 부여한다.
N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.

학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
K 번째 학생의 학점을 출력하는 프로그램을 작성


필수조건:
#
딕셔너리로 입력받는 순서대로 번호를 매긴 후,
총점으로 sort하고,
그후 함수로 만든 평가에 알파벳으로 반환값을 준다.

즉, 알파벳은 받은학생수/10 의 비율로 정해지므로, 해당 값을 만큼 알파벳들을 리스트로 받아서 준비하고,
이에따라 반환값이 주어진다.

A+
A0
A-
B+
B0
B-
C+
C0
C-
D0

'''


'''
Test Data
T = 1
N = 10 # 학생수
K = 2 # 학점을 알고싶은 학생의 번호

중간 기말 과제
87 59 88
99 94 78
94 86 86
99 100 99
69 76 70
76 89 96
98 95 96
74 69 60
98 84 67
85 84 91

'''

for T in range(int(input())):

    N, K = map(int,input().split()) # 항상 10의 배수 10 <= N <= 100  # 1이상 N이하의 정수 1 <= K <= N
                    # K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.
    scores_board = []
    student_dict = {}
    sorted_board = []

    alphabet = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    alphabet_list = []

    for grade in alphabet:
        for i in range(N//10): #받은 학생수만큼 10을 나눈 몫으로 range를 구해서 리스트에 비율만큼의 알파벳을 넣는다.
            alphabet_list.append(grade)
    #print(alphabet_list)

    for i in range(N):
        scores = list(map(int, input().split()))
        scores_board.append(scores)
        # print(scores_board)
        # [['87', '59', '88'], ['99', '94', '78']]
        # 2차원 배열을 만든다.
        # 학생 수 만큼 돌면서 총점을 구한다.
        try:
            totalScore_student = scores_board[i][0]*0.35 + scores_board[i][1]*0.45 + scores_board[i][2]*0.20
            student_dict[totalScore_student] = i+1
            print(student_dict)

            # {1: 74.6, 2: 92.55000000000001, 3: 88.8, 4: 99.45, 5: 72.35, 6: 85.85000000000001, 7: 96.25, 8: 68.95, 9: 85.5, 10: 85.75}
            # {74.6: 1, 92.55000000000001: 2, 88.8: 3, 99.45: 4, 72.35: 5, 85.85000000000001: 6, 96.25: 7, 68.95: 8, 85.5: 9, 85.75: 10}
            print(student_dict[1]) # 74.6
        except:
            continue

    student_dict_sorted = dict(sorted(student_dict.items(), reverse=True)) # 내림순으로 순서를 정렬한 딕셔너리를 만든다.
    #print(student_dict_sorted)
    # [(99.45, 4), (96.25, 7), (92.55000000000001, 2), (88.8, 3), (85.85000000000001, 6), (85.75, 10), (85.5, 9), (74.6, 1), (72.35, 5), (68.95, 8)]
    # {99.45: 4, 96.25: 7, 92.55000000000001: 2, 88.8: 3, 85.85000000000001: 6, 85.75: 10, 85.5: 9, 74.6: 1, 72.35: 5, 68.95: 8}

    # 딕셔너리 내의 값과 알고싶은 학생번호가 같을 때의 알파벳리스트에서 리스트를 인덱스로 찾아온다.
    count = 0 # 이를 위해서 count를 설정하여 한 번 돌때마다 더해줘서 인덱스를 찾을 수 있도록 설정해준다.
    for key, value in student_dict_sorted.items():
        count += 1
        if value == K:
            print(f'#{T+1} {alphabet_list[count-1]}') #인덱스는 0부터 시작하기때문에 돈만큼에서 -1을 해줘야 한다.
