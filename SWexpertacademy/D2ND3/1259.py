import sys
sys.stdin = open('1259.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 3
    stick = list(map(int, input().split()))
    big_board = []

    #2개씩 나눠서 만들어준다.
    for ix in range(N): # 0, 1
        small_board = []
        for i in range(2):
            small_board.append(stick[ix*2+i]) # 0, 1
        #print(small_board)
        big_board.append(small_board)
    #print(big_board)

    new_list = [big_board[0]]
    #print([big_board[0]])  # [[3, 4]]
    big_board.pop(0)

    while big_board != []:
        for standard in big_board:
            if standard[0] == new_list[-1][1]:
                new_list.append(standard)
                big_board.remove(standard)

            elif standard[1] == new_list[0][0]:
                new_list.insert(0, standard)
                big_board.remove(standard)

    print(f'#{tc}', end=' ')
    for i in range(N):
        for ix in range(2):
            print(f'{new_list[i][ix]}', end=' ')
    print()#하나만 맞으면 시퀀스가 완성된다.
