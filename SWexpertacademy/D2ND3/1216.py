import sys
sys.stdin = open('1216.txt', 'r')

'''
list.reverse()
words[-1]
'''

'''
직선 회문만 비교하기때문에

열과
행
두가지로
비교

1) 행비교
2) zip으로 열에대한 세로를 가로로 만들어서 비교


word의 처음 i라는 인덱스에 +1씩해가면서 비교한다.
그리고 그 비교한 것 중에 맞는것에 대한 숫자를
리스트에 넣고
맨 마지막에 max하여 가장 긴 길이를 찾는다.
'''

'''
그러면 보드를 만드는것부터 시작
'''
def Columntorow(arr, N):
    result = []
    for iy in range(N):
        new = []
        for ix in range(N):
            new.append(arr[ix][iy])
        result.append(new)
    #print(result)
    return result


def Search(arr, N):
    num_list = []
    for ar in arr:
	# idx 부터 idx+idx2 까지가 아니라 idx 부터 idx2까지 검색하기
        for idx in range(0, N-1):
            for idx2 in range(idx+1, N+1):
                temp = ar[idx:idx2]
                if ar[idx:idx2] == temp[::-1]:
                    num_list.append(len(temp))
    return set(num_list)

for tc in range(10):
    T = int(input())
    N = 100

    sentences = []

    for i in range(N):
        temp = list(map(str, input()))
        sentences.append(temp)

    result1 = Search(sentences, N)

    new_sentences = Columntorow(sentences, N)

    result2 = Search(new_sentences, N)

    result3 = list(result1) + list(result2)

    print(f'#{T} {max(result3)}')