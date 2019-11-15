import sys
sys.stdin = open('4012.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    def combiAndPerm(k, s):
        global mymin
        if k == R:
            # 구한 집합을 가지고 작업
            firstnum = 0
            secondnum = 0
            second = list( set([i for i in range(N)]) - set(first) )

            # 구한 집합에서 순열을 구한 후 시너지를 구한다.
            for i in range(R-1):
                for j in range(i+1, R):
                    # print(i, j)
                    firstnum += (arr[first[i]][first[j]] + arr[first[j]][first[i]])

            for i in range(R-1):
                for j in range(i+1, R):
                    secondnum += (arr[second[i]][second[j]] + arr[second[j]][second[i]])
            mymin = min(mymin, abs(firstnum-secondnum))
            return

        else:
            # 두 집합을 구한다.
            for i in range(s, N-R+k+1):
                first[k] = i
                combiAndPerm(k+1, i+1)

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    R = N//2
    first = [0]*R
    mymin = 1e9
    combiAndPerm(0,0)
    print(f'#{tc} {mymin}')

