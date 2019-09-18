import sys
sys.stdin = open('5203.txt', 'r')



T = int(input())
for tc in range(1, T+1):

    cards = list(map(int, input().split()))


    #countingsort로 빈도수 계
    firstplayer = [0]*10
    secondplayer = [0]*10
    for idx in range(12):
        if idx%2 == 0:
            firstplayer[cards[idx]] += 1
            # print(cards[idx])
        if idx%2 == 1:
            secondplayer[cards[idx]] += 1



    flag = 0
    # run과 triple 여부 판단
    # 조사는 총 두번
    # 연속적으로 앞에 있어서 총 3이 되면 run
    # 카운트 소트에서 삭제
    # 남은거에서 3이 있므면 triple
    run_ = 0
    for idx in range(8):
        if firstplayer[idx] > 0 and firstplayer[idx+1] > 0 and firstplayer[idx+2] > 0:
            run_ = 1
            if run_ == 1:
                flag = 1
                firstplayer[idx] -= 1
                firstplayer[idx+1] -= 1
                firstplayer[idx+2] -= 1

        if secondplayer[idx] > 0 and secondplayer[idx+1] > 0 and secondplayer[idx+2] > 0:
            run_ = 1
            if run_ == 1:
                flag = 2
                secondplayer[idx] -= 1
                secondplayer[idx+1] -= 1
                secondplayer[idx+2] -= 1

    triple = 0
    for idx in range(10):
        if firstplayer[idx] == 3:
            flag = 1

        if secondplayer[idx] == 3:
            flag = 2

    print(f'#{tc} {flag}')

