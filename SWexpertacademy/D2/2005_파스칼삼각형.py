# 2005
'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE
'''

T = int(input())
for tc in range(1, T+1):
    row = int(input())
    print(f'#{tc}')
    for rownum in range(row):
        list = 1
        Plist = [list]
        print('1', end=' ')
        for i in range(rownum):
            list = list*(rownum-i)*1/(i+1)
            Plist.append(int(list))
            print(str(int(list)), end=' ')
        print()

'''
https://m.blog.naver.com/PostView.nhn?blogId=vollollov&logNo=220947452823&proxyReferer=https%3A%2F%2Fwww.google.com%2F
첫줄은 숫자 1
두번째 줄부터 각 숫자들은 위 오른쪽과 왼쪽의 합이다.

파스칼 삼각형을 생성한다.
'''

'''
>> > a = [1, 2, 3]
>> > a[len(a):] = [10]
>> > a
[1, 2, 3, 10]
temp_list_b = []
for T in range(1):
    pass
    for t in range(1, 5):

        if t == 1:
            print(1) # 1이 나옴
        elif t == 2:
            for i in range(2):
                temp_list_b.append(1)
            print(temp_list_b) # [1, 1]이 나옴
        else: 
            temp_list_a = [1]
            for d in range(1, t-1):
                print('--------')

                a = temp_list_b[d-1] + temp_list_b[d]
                print('a1', a) #3이 나왔을때 1과 2 index에 넣어줘야 한다.

                temp_list_a.append(a)
                print(temp_list_a)
                #temp_list_b.insert(t, a)

                print(temp_list_b)
            #temp_list_a    
'''

