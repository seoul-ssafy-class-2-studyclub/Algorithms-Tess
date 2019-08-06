def BinarySearch(P, Pab):
    book = [i for i in range(P + 1)]  # 순서대로 정렬 1, 2, 3 ... 400

    start = 1
    end = P
    cnt = 0

    while start <= end:
        middle = int((start + end) / 2)  # 200

        if Pab == book[middle]:
            return cnt
            break

        elif Pab < book[middle]:
            end = middle
            cnt += 1

        elif Pab > book[middle]:
            start = middle
            cnt += 1

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnta = BinarySearch(P, Pa)
    cntb = BinarySearch(P, Pb)

    if cnta < cntb:
        print('#{} A'.format(tc))
    elif cnta > cntb:
        print('#{} B'.format(tc))
    elif cnta == cntb:
        print('#{} 0'.format(tc))