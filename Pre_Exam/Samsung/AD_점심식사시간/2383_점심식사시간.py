import sys
sys.stdin = open('2383.txt', 'r')
'''
#1 9
#2 8
#3 9
#4 7
#5 8
#6 8
#7 11
#8 11
#9 18
#10 12


2. 방의 한 변의 길이 N은 4 이상 10 이하의 정수이다. (4 ≤ N ≤ 10)
3. 사람의 수는 1 이상 10 이하의 정수이다. (1 ≤ 사람의 수 ≤ 10)
4. 계단의 입구는 반드시 2개이며, 서로 위치가 겹치지 않는다.
5. 계단의 길이는 2 이상 10 이하의 정수이다. (2 ≤ 계단의 길이 ≤ 10)
6. 초기에 입력으로 주어지는 사람의 위치와 계단 입구의 위치는 서로 겹치지 않는다.
'''


















import itertools
import heapq


# def makeWaitinglist(ft, fm, fdinfo, data):
#     onWaiting = []
#     ftemp = ft
#     onWaiting.append([ft, fm, fdinfo])
#     while data and len(onWaiting) != 4:
#         tem, ftm, ftmfinfo = data.pop(0)
#         if ftemp == tem:
#             onWaiting.append([tem, ftm, ftmfinfo])
#         elif ftemp != tem:
#             break
#     print(onWaiting, data)
#     return onWaiting, data
'''
- 3명까지
    리스트의 최대길이는 3
    불러온다
    세워는 놓는데
    현재시간하고 비교하면서 넣을지 말지 생각해야한다..
    리스트는 큐
    넣은 순간부터 2라는건 중요하지 않다.
    계단에 들어왔을때는 계단을 갈때 걸리는 시간이다
    
    리스트안에있는 애들은
    현재 길이만큼 반복문을 도는데
    1초의 과정이다.
    
    1 2 3 이라는 배열이 될때
    1이면 나와야한다. 왜냐하면 0이 되니까
    리스트 길이기 2가되면 들어오게 된다.
'''
def solve(first, second):
    global mymin, doors, firstmins, secondmins
    firstdatas = []
    seconddatas = []
    for fir in first:
        time = abs(fir[0] - doors[0][0]) + abs(fir[1] - doors[0][1])
        firstdatas.append([time, firstmins, doors[0]])
    for sec in second:
        time = abs(sec[0] - doors[1][0]) + abs(sec[1] - doors[1][1])
        seconddatas.append([time, secondmins, doors[1]])
    seconddatas = sorted(seconddatas)
    firstdatas = sorted(firstdatas)

    # 둘 다 빌때까지 진행한다.
    # 앞에서 부터 빼는데, 처음 뺀 것의 시간과 같지 않은게 나올때까지 뺀다.
    # 따로 관리하는게 마음 편할 듯

    # waiting_list = [firstdatas, seconddatas]
    # t = -1
    # while doors[0] or doors[1] or firstdatas or seconddatas:
    #     t += 1
    #
    #     for i in range(2):
    #         for _ in range(len(doors[i])):
    #             temp = doors[i].pop(0)
    #             if temp == doors[i][2] - 1:
    #                 continue
    #
    #             doors[i].append(temp + 1)
    #
    #         while waiting_list[i] and len(doors[i]) < 3:
    #             if waiting_list[i][0] <= t:
    #                 waiting_list[i].pop(0)
    #                 doors[i].append(0)
    #             else:
    #                 break
    #
    # if t < mymin:
    #     mymin = t


    # 애초에 waitinglist에 같은 시간에 도착하고, 3이하인 애들만 들어오게 만들었으니까
    # 내려보내면서 -1씩 처리해가야 한다.
    # 내려간 애들의 수가 3보다 작아지면 이제 또 다른 애들을 추가 할 수 있게 되는거임.




'''
나눈 후보들을 가지고 아래를 시작하면 되는데.. 생각해보자

① 계단 입구까지 이동 시간
        - 사람이 현재 위치에서 계단의 입구까지 이동하는데 걸리는 시간으로 다음과 같이 계산한다.
        - 이동 시간(분) = | PR - SR | + | PC - SC |
          (PR, PC : 사람 P의 세로위치, 가로위치, SR, SC : 계단 입구 S의 세로위치, 가로위치)

② 계단을 내려가는 시간
    - 계단을 내려가는 시간은 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간이다.
    - 계단 입구에 도착하면, 1분 후 아래칸으로 내려 갈 수 있다.
    - 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있다.
    - 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 한다.
    - 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K 분이 걸린다.
    
'''


T = int(input())

for tc in range(1, T-8):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # data를 찾는 코드
    doors = []
    people = []
    for R in range(N):
        for C in range(N):
            if board[R][C] == 1:
                people.append((R, C))
            if board[R][C] > 1:
                doors.append((R, C, board[R][C]))
    firstmins = board[doors[0][0]][doors[0][1]]
    secondmins = board[doors[1][0]][doors[1][1]]
    # numbers를 가져오는 코드
    numofPeople = len(people)
    numofCandidate = [i for i in range(numofPeople)]

    # 경우의 수를 추출하기 위한 후보들을 찾는 코드
    gotoFirstDoor = []
    for i in numofCandidate:
        temp = list(itertools.combinations(people, i))
        gotoFirstDoor.append(temp)
    mycandidates = []
    for i in gotoFirstDoor:
        for i in i:
            temp = set(people) - set(i)
            mycandidates.append((list(temp), i))
    # mycandidates 에 담겨있는 애들로 시작할건데,
    # door가 두개이므로 door1에 했던걸 door2에도 해줘야 한다.

    mymin = 9999999
    for i in mycandidates:
        solve(i[0], i[1])
        solve(i[1], i[0])



    # 도어의 수에 맞게 그룹을 나눠준다.
    # 전제조건에서 계단 입구는 항상 2개뿐이므로
    # people만 두그룹으로 나누는 경우의 수를 구하면 된다.


'''
def permutaion(arr):
    if len(arr) == P:
        stair_choice.append(arr)
        return
     
    for i in range(2):
        permutaion(arr + [i])
     
for ro in range(int(input())):
    N = int(input())
 
    board = []
    for _ in range(N):
        board.append(list(map(int,input().split())))
     
    people = []
    stairs = []
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                people.append((y, x))
            elif board[y][x] > 1:
                stairs.append((y, x, board[y][x]))
     
    P = len(people)
    stair_choice = []
    permutaion([])
    res = 999999
    waiting_1 = []
    waiting_2 = []
    waitings_list = [waiting_1, waiting_2]
    stair_1 = []
    stair_2 = []
    stairs_list = [stair_1, stair_2]
 
    while stair_choice:
 
        choices = stair_choice.pop(0)
        for i in range(P):
            dy = abs(people[i][0] - stairs[choices[i]][0])
            dx = abs(people[i][1] - stairs[choices[i]][1])
            waitings_list[choices[i]].append(dy + dx)
         
        waiting_1.sort()
        waiting_2.sort()
        t = -1
        while stair_1 or stair_2 or waiting_1 or waiting_2:
            t += 1
 
            for i in range(2):
                for _ in range(len(stairs_list[i])):
                    temp = stairs_list[i].pop(0)
                    if temp == stairs[i][2] - 1:
                        continue
 
                    stairs_list[i].append(temp + 1)
 
                while waitings_list[i] and len(stairs_list[i]) < 3:
                    if  waitings_list[i][0] <= t:
                        waitings_list[i].pop(0)
                        stairs_list[i].append(0)
                    else: break
                 
        if t < res:
            res = t
 
    print('#%d %d' %(ro+ 1, res + 1))
'''