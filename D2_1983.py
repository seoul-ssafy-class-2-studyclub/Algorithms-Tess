alphabet = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for T in range(int(input())):

    N, K = map(int, input().split())
    scores_board = []
    student_dict = {}
    sorted_board = []
    alphabet_list = []

    for grade in alphabet:
        for i in range(N // 10):
            alphabet_list.append(grade)

    for i in range(N):
        scores = list(map(int, input().split()))
        scores_board.append(scores)

        try:
            totalScore_student = scores_board[i][0] * 0.35 + scores_board[i][1] * 0.45 + scores_board[i][2] * 0.20
            student_dict[totalScore_student] = i + 1
        except:
            continue

    student_dict_sorted = dict(sorted(student_dict.items(), reverse=True))

    count = 0

    for key, value in student_dict_sorted.items():
        count += 1
        if value == K:
            print(f'#{T + 1} {alphabet_list[count - 1]}')
