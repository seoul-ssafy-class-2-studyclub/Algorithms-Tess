import sys
sys.stdin = open('scratch4.txt', 'r')

# 동시에 움직이고,
# 다 움직이면,
# 움직인 결과 같이 겹치면,
# 그 겹친애들은 죽어서
# 상태가 바뀌고,
# 상태가 바뀐 애들의 k만 더하면 총합이 나온다.


# 클래스로 각각의 원소들의 정보를 저장하고 x, y를 더해나가다가
# 동일한 x, y가 changed_xandy안에서 발견되면 해당 원소가 가진 k를 return 한다.
class Collision():

    def __init__(self, name, x, y, d, k):
        self.name = 0
        self.x = 0
        self.y = 0
        self.d = 0
        self.k = 0
        self.status = True

    def moving(self, x, y):
        self.x = self.x+dx[self.d]
        self.y = self.y+dx[self.d]
        return (self.y, self.x)


    def check(self, x, y, other):
        if self.status == False:
            total_K += self.k
            return total

def check():
    pass

def moving(y, x, d):
    x = x+dx[d]
    y = y+dy[d]
    return y, x


# 방향 설정
# 상(0), 하(1), 좌(2), 우(3)
dy = [0.5, -0.5, 0, 0]
dx = [0, 0, -0.5, 0.5]

# dy = [1, -1, 0, 0]
# dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):

    N = int(input()) # 원자들의 수
    # NAME = [None]+[x for x in range(1, N+1)]
    Alive = [None]+[True]*(N+1)
    # 각 원자들은 앞으로 인덱스로 분류된다.

    X_list = [None]+[]
    Y_list = [None]+[]
    D_list = [None]+[]
    K_list = [None]+[]

    for idx in range(1, N+1):
        X, Y, D, K = map(int, input().split())
        # atom = Collision(NAME[idx], X, Y, D, K)
        X_list.append(X)
        Y_list.append(Y)
        D_list.append(D)
        K_list.append(K)

    # print(X_list)
    # print(Y_list)
    # print(D_list)
    # print(K_list)

# 종료조건
# 소멸될 애들은 다 소멸되고, 남은 원소들이 다른 원소와 부딪힐 가능성이 없다고 판단되는 경우 즉, 더이상 소멸될 애들이 없어
# 시간이 흐르면 좌표를 벗어나는 이동을 할 것이라 판단되면 종료한다.
# 이게 종료조건
# 하지만 하나의 애들만 그런것이 아니라 남은 모든 애들이 그럴 경우여야 한다.

# 소멸시키고, 소멸되는 2 이상의 원소들이 가진 에너지를 모두 더한다.
# 소멸되는 조건은 동일한 시간이 지났을때, 동일한 좌표에 도착했을 경우

    flag = True
    
    while flag == True:
        if flag == False:
            break
        try:
            for i in range(4002):
                #print('{}'.format(tc, i))
                if i == 4001:
                    flag = False
                    break
                else:
                    # moving이 완료되고,
                    for idx2 in range(1, N+1):
                        D = D_list[idx2]
                        y, x = moving(Y_list[idx2], X_list[idx2], D)
                        X_list[idx2] = x
                        Y_list[idx2] = y
                    # 체크하고, 반복
                    for idx3 in range(1, N+1):
                        for idx4 in range(idx3+1, N+1): # 0 1, 2
                            if X_list[idx3] == X_list[idx4] and Y_list[idx3] == Y_list[idx4] and D_list[idx3] != D_list[idx4] and Alive[idx3] == True and Alive[idx4] == True:
                                Alive[idx3] = False
                                Alive[idx4] = False
        except:
            print('error')
    
    total_K = 0 # Alive에서 False 된 애들만 total_K에 해당 index로 list_K값을 찾아서 더해준다.
    for idx5 in range(1, N+1):
        print(Alive)
        if Alive[idx5] == False:
            print(K_list[idx5])

            total_K += K_list[idx5]
            K_list[idx5] = 0
    print('#{} {}'.format(tc, total_K))

            
            
        
               



    
