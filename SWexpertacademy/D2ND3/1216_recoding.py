import sys
sys.stdin = open('1216.txt', 'r')
#
# def Columntorow(arr, N):
#     result = []
#     for iy in range(N):
#         new = []
#         for ix in range(N):
#             new.append(arr[ix][iy])
#         result.append(new)
#     return result
#
#
# def Search(arr, N):
#     num_list = []
#
#     for ar in arr:
#         for idx in range(0, N-1):
#             for idx2 in range(idx+1, N+1):
#                 temp = ar[idx:idx2]
#                 if ar[idx:idx2] == temp[::-1]:
#                     num_list.append(len(temp))
#     return set(num_list)
#
# for tc in range(10):
#     T = int(input())
#     N = 100
#     sentences = []
#
#     for i in range(N):
#         temp = list(map(str, input()))
#         sentences.append(temp)
#
#     new_sentences = Columntorow(sentences, N)
#     result1, result2 = Search(sentences, N), Search(new_sentences, N)
#     result3 = list(result1) + list(result2)
#     print(f'#{T} {max(result3)}')


def Palindrom(str, length):
    for i in range(100): # 100번을 돌면서,
        for idx in range(101 - length): # 101-21, 101-20,,,,
            for k in range(length // 2): # 21//2 -> 10.5
                if str[i][idx + k] != str[i][idx + length - 1 - k]:
                    break
                elif k + 1 == (length // 2):
                    return length
            for k in range(length // 2):
                if str[idx + k][i] != str[idx + length - 1 - k][i]:
                    break
                elif k + 1 == (length // 2):
                    return length
    return 0


for _ in range(10):
    print('#' + input(), end=' ')
    arr = [input() for i in range(100)]  # 100 rows

    for i in range(21, 0, -1): #뒤에서 -1씩 21부터 0까지, 21, 20, 19, 18,,,,
        length = Palindrom(arr, i)
        if length:
            print(length)
            break