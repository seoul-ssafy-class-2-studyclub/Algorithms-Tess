import sys
sys.stdin = open('4861.txt', 'r')


#########회문이 뭔지 찾는 문제
from pprint import pprint

def column(arr, N):

    new_row = []
    for iy in range(N):
        new = []
        for ix in range(N):
            new.append(arr[ix][iy])
        new_row.append(new)
    return new_row


def Search(arr, N, M):

    B = N - M

    for idx in range(0, B+1): # 0, 8 0 1 2 3 4 5 6 7
        temp = arr[idx:idx+M] # 0:13, 1:14, 2:16, 3:17, 4:18, 5:19, 6:20, 7:21
        #print(temp)
        if arr[idx:idx+M] == temp[::-1]:
            #print(temp)
            result = temp
            return ''.join(result)
        else:
            result = False
    return result ## for문을 다 돌고 나서도 없을 경우 빠져나오게 바깥으로!


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    '''
    N*N 보드판
    M 찾으려는 글자수
    '''
    sentences = []
    for n in range(N):
        sentences.append(list(map(str, input())))
    #print(sentences)

    result = False
    if result == False:
        for sentence in sentences:
            result = Search(sentence, N, M)
            if result != False:
                print(f'#{tc} {result}')


    if result == False:
        columntorow = column(sentences, N)
        for second_sentence in columntorow:
            result = Search(second_sentence, N, M)
            if result != False:
                print(f'#{tc} {result}')








