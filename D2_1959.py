'''

두 개의 숫자

B를 고정시키고
A열을 한칸씩 움직여가며
B의 인덱스를 옮기면서
곱한값과 더한값을 리스트에 넣고
Max를 써서 찾는다.

Count써서 특정 3이될경우 계속 반복하고
애초에 들어올때 b의 문자열보다 작은 인덱스사 필요하고

'''

for t in range(int(input())): # 10
    #t = 1 # 10
    Ai, Bi = map(int, input().split())
    # A의 index # B의 index

    '''
    1 5 3
    3 6 -7 5 4
    
    #1 30
    '''

    A = list(map(int, input().split())) # [1, 5, 3]
    B = list(map(int, input().split())) # [3, 6, -7, 5, 4]

    temp_list = []
    sum_list = []

    IndexForTotal_Bi = Bi - 2
    IndexForTotal_Ai = Ai - 2

    try:
        if Ai < Bi: # Bi가 더 큰 경우 Ai의 인덱스는 고정된다.
            count = 0
            for Idx in range(IndexForTotal_Bi):
                total = 0
                Idx += count

                for Idx_Ai in range(Ai):
                    C = B[Idx+count] * A[Idx_Ai]
                    count += 1
                    temp_list.append(C)

                sum_list = sum(temp_list)

            print(temp_list)
            print(f'#{t + 1} {max(sum_list)}')


        else:
            count = 0
            for Idx in range(IndexForTotal_Ai):
                total = 0
                Idx += count

                for Idx_Bi in range(Bi):
                    C = B[Idx_Bi] * A[Idx+count]
                    temp_list.append(C)

                sum_list = sum(temp_list)

            print(temp_list)
            print(f'#{t + 1} {max(sum_list)}')



    except IndexError:
        continue




