
'''

순서대로 작업의 진도가 적힌 정수 배열 progresses와
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때

각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성

'''


# 작업의 개수는 100개 이하
'''
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.

배포는 하루에 한 번만 할 수 있으며, 
하루의 끝에 이루어진다고 가정합니다. 

예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 
94 -> 103 ( 100이 넘어간다 )
배포는 2일 뒤에 이루어집니다.


첫 번째 기능은 93% 완료되어 있고 
하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.

두 번째 기능은 30%가 완료되어 있고 
하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 
하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 
첫 번째 기능이 배포되는 7일째 배포됩니다. (준비상태로 있으면 된다)

세 번째 기능은 55%가 완료되어 있고 
하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.


따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

(동시적으로 퍼센트만큼올라가고, 앞에가 100 이상이 되는 순간 차례로 뺀다.
빼는걸 검사하면서 올린다 = >  1일씩 추가)
'''

import collections
def solution(progresses, speeds):
    # test = zip(progresses, speeds)
    # print(test)
    # for p, s in test:
    #     print(p, s)
    data = collections.deque([])
    N = len(progresses)
    for i in range(N):
        data.append([progresses[i], speeds[i]])
    print(data)
    # 빌때 까지
    release = 0
    answer = []
    while data:
        # 이 데이터가 다 빌때까지

        for i in range(len(data)):
            data[i][0] += data[i][1]

        while data:
            temp = data.popleft()
            if temp[0] < 100:
                data.appendleft(temp)
                break
            if temp[0] >= 100:
                release += 1
        if release != 0:
            answer.append(release)
            release = 0
    return answer


solution([93,30,55], [1,30,5])