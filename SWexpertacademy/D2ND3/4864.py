import sys
sys.stdin = open('4864.txt', 'r')

# 보이어 무어 알고리즘 활용!

T = int(input())
for tc in range(1, T+1):
    #print(tc)
    target = list(map(str, input()))
    # ['X', 'Y', 'P', 'V']
    sentence = list(map(str, input()))
    # ['E', 'O', 'G', 'G', 'X', 'Y', 'P', 'V', 'S', 'Y']
    #print(target, sentence)

    '''
1) 패턴 오른쪽 끝 문자와 텍스트의 현재 위치 문자가 일치하는지 검사하기 위해 회문으로 만든다.
2) 끝이 일치하면 패턴과 텍스트를 모두 검사, 마지막까지 일치하지 않으면 패턴길이만큼 스킵
3) 끝이 일치하지 않으면 텍스트의 현재 위 문자가 스킵배열에 있는지 확인
있으면 인덱스 만큼 스킵, 없으면 패턴 길이만큼 스킵
4) 텍스트 큰 도달할 때 까지 반복
    '''

    ## 보이어 무어 알고리즘 시작
    target_reversed = target[::-1]
    idx = len(target) - 1 # 3 마지막 인덱스를 위해서
    result = 0

    while idx < len(sentence): ## 4 < 10 ### 8
        next = len(target_reversed) # 4
        j = 0

        if target_reversed[j] == sentence[idx]: # V == G ## V == X
            while j < len(target_reversed):
                if target_reversed[j] != sentence[idx-j]:
                    break
                j += 1
            if j == len(target_reversed):
                result = 1 # 모두 검사했을때 동일하면, result에 1을 저장한다.

        else:
            while j < len(target_reversed): # 0
                if target_reversed[j] == sentence[idx]: # V == G
                    next = min(j, next)

                j += 1 # 위가 False이므로 j가 4를 넘을때까지 반복한다.

        if result: # 1 이라면, True 라면, 여전히 0이므로 아래를 실행하고,
            break

        idx += next # 4를 i넣어서 4만큼 건너 뛴다. ### 8


    print(f'#{tc} {result}')
