import sys
sys.stdin = open('4047.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    cards_total = {'S': 13, 'D':13, 'H':13, 'C':13}

    cards = list(map(str, input()))
    list_len = len(cards)
    big_board = []
    result = ''

    for ix in range(list_len//3): #0 1 2 3
        new = []
        for i in range(3): # 0 1 2
            new.append(cards[ix*3+i]) # 0*2+0
        big_board.append(new)

    big_board_len = len(big_board)
    for idx in range(big_board_len):
        cards_total[big_board[idx][0]] -= 1

    for idx in range(0, big_board_len-1):
        for idx2 in range(idx+1, big_board_len): ## 중요!!!
            if big_board[idx] == big_board[idx2]:
                result = 'ERROR'

    if result != 'ERROR':
        result = '#{} {} {} {} {}'.format(tc, cards_total['S'], cards_total['D'], cards_total['H'], cards_total['C'])
        print(result)
    else:
        print('#{} ERROR'.format(tc))

