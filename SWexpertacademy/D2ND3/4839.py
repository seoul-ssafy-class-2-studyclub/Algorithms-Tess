import sys
sys.stdin = open('4839.txt', 'r')




T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    book = [i for i in range(P+1)]  # 순서대로 정렬 1, 2, 3 ... 400

    start = 1
    end = P  # 400
    cnta = 0

    while start <= end:
        middle = int((start + end) / 2)   # 200
        #print('a', start, end, middle)

        if Pa == book[middle]:
            break

        elif Pa < book[middle]:
            end = middle - 1
            cnta += 1

        elif Pa > book[middle]:
            start = middle + 1
            cnta += 1

    start = 1
    end = P # 399
    cntb = 0

    while start <= end:

        middle = int((start + end) / 2)  # 0
        #print('b', start, end, middle)

        if Pb == book[middle]:
            break

        elif Pb < book[middle]:
            end = middle - 1
            cntb += 1

        elif Pb > book[middle]:
            start = middle + 1
            cntb += 1

    if cnta < cntb:
        print('#{} A'.format(tc))
    elif cnta > cntb:
        print('#{} B'.format(tc))
    elif cnta == cntb:
        print('#{} 0'.format(tc))

    # 먼저 찾는 애가 되어야 한다?

'''
T = int(input())
for t in range(T):
   P, Pa, Pb = list(map(int,input().split()))
   l, r, c, cnt_a, cnt_b = 1, P, 0, 0, 0
   while True:
       if c == Pa:
           break
       c = int((l+r)/2)
       cnt_a += 1
       if Pa > c:
           l = c
       else:
           r = c
   l, r = 1, P
   while True:
       if c == Pb:
           break
       c = int((l+r)/2)
       cnt_b += 1
       if Pb > c:
           l = c
       else:
           r = c
   print('#{}'.format(t+1), end=' ')
   if cnt_a < cnt_b:
       print('A')
   elif cnt_b < cnt_a:
       print('B')
   else:
       print(0)

'''