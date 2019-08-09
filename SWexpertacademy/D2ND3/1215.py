import sys
sys.stdin = open('1215.txt', 'r')

## 회문의 개수를 구하는 문제


def Columntorow(arr, N):
    columntorow = []
    for iy in range(N):
        new = []
        for ix in range(N):
            new.append(arr[ix][iy])
        columntorow.append(new)
    return columntorow

def Palindrome(arr, N, M):
    B = N - M
    cnt = 0
    for ar in arr:
        for idx in range(0, B+1):
            temp = ar[idx:idx+M]
            if ar[idx:idx+M] == temp[::-1]:
                if True:
                    cnt += 1
    return cnt

for tc in range(1, 11):
    N = 8
    M = int(input())
    sentences = []
    for n in range(N):
        sentences.append(list(map(str, input())))
    rowcnt = Palindrome(sentences, N, M)
    new_sentences = Columntorow(sentences, N)
    columncnt = Palindrome(new_sentences, N, M)
    totalcnt = rowcnt + columncnt
    print(f'#{tc} {totalcnt}')




#
#
#
# def Columntorow(arr, N):
#
#     columntorow = []
#     for iy in range(N):
#         new = []
#         for ix in range(N):
#             new.append(arr[ix][iy])
#         columntorow.append(new)
#     return columntorow
#
#
# def Palindrome(arr, N, M):
#     B = N - M
#
#     cnt = 0
#     for ar in arr:
#         for idx in range(0, B+1):
#             temp = ar[idx:idx+M]
#             if ar[idx:idx+M] == temp[::-1]:
#                 if True:
#                     cnt += 1
#     #print('cnt', cnt)
#     return cnt
#
#
# for tc in range(1, 11):
#     N = 8
#     M = int(input())
#
#     sentences = []
#     for n in range(N):
#         sentences.append(list(map(str, input())))
#
#     #print(sentences)
#
#
#     rowcnt = Palindrome(sentences, N, M)
#     #print('1', rowcnt)
#
#     new_sentences = Columntorow(sentences, N)
#     #print('1', sentences, '2', new_sentences)
#
#     columncnt = Palindrome(new_sentences, N, M)
#     #print('2', columncnt)
#     #print(rowcnt, columncnt)
#
#     totalcnt = rowcnt + columncnt
#
#     print(f'#{tc} {totalcnt}')
