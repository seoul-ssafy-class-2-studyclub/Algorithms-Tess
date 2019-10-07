import sys
sys.stdin = open('1808.txt', 'r')

'''
0 1 1 0 0 1 0 0 0 0
1,2,5,*,=를 사용해서 60만들기


#1 6
#2 8
#3 7
#4 6
#5 10
#6 7
#7 -1
#8 11
'''


def isPrime(g):
    a = [False, False] + [True]*(g-1)
    primes = []
    for i in range(2, g+1):
        if a[i]: # True라면
            primes.append(i)
            for j in range(2*i, g+1, i):
                a[j] = False
    return a

def search(nums, mults):
    global mylist

    nums = str(nums)
    mults = str(mults)
    cnt = 0
    for char in nums:
        if char in mylist:
            cnt += 1
    cnt2 = 0
    for char in mults:
        if char in mylist:
            cnt2 += 1
    if cnt == len(nums) and cnt2 == len(mults):
        return cnt + cnt2 + 1, nums, mults

    else:
        return False, nums, mults



def solve(g):
    global mymin, myminnums, myprimes


    if myprimes[int(g)] == True:
        return

    # 모든 약수를 구한다.
    # 약수를 구할때마다 mylist에 있는지, 모든 경우가 확인하고 있으면 1을 한다.
    # 1을 하고나면 결과를 mymin에 갱신한다.
    # 소수인 경우인지 항상 확인하는 탈출조건을 만들어준다.
    # 루트 int(goal ** 0.5 + 1) 구하기

    for i in range(2, int(int(g) ** 0.5 + 1)):
        # 1~루트 (g+1) 까지 돌면서, 약수를 구한다.
        if int(g) % i == 0:
            main = int(g)//i
            multiple = i

            # 3. 약수를 구해서 자판기에 있는 숫자라면 1을 더하는 함수
            num, n, m = search(main, multiple)
            if mymin > num and num != False:
                mymin = num
                myminnums.append((n, m))

            elif num == False:
                solve(main)
                solve(multiple)
                # 그 아래에서 쪼갤때의 숫자들이 goal의 숫자를 만들 수 있을까?를 고려해야한다.



for tc in range(int(input())):
    temp = list(map(str, input().split()))
    goal = input()

    # 가능한 숫자로 변환한다.
    mylist = []
    for i in range(len(temp)):
        if temp[i] == '1':
            mylist.append(str(i))
    # 2. goal으로 부터 먼저 에라토스테네스의 체를 이용하여 소수구하는 함수
    '''
    소수: 소수(Prime Number)는 약수로 1과 자기 자만을 가지는 정수
    에라토스테네스의 체: 
    범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 
    1. 1은 제거 
    2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다. 
    3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다. 
    4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다. 
    5. (반복)     
    '''
    myprimes = isPrime(int(goal)) # 남은 True가 소수이다.

    # 1. 약수구하는 함수
    # 약수는 숫자%i == 0 이되는 i와 숫자//i 를 말한다.
    # 60일때 12 * 5는 '2번' '*' '1번' '=' 총 5번을 누른다.
    # 자판기에서 선택 가능한 숫자들이 나올텐데, 그게 가능한 모든 경우의 수를 다 검사를 해야만,
    # 우리가 원하는 최소값을 찾을 수 있다.
    mymin = 99999
    myminnums = []
    solve(goal)

    print(f'#{tc+1}', mymin, myminnums)








