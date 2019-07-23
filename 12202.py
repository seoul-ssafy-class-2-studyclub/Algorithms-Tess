for T in range(1, 11):
    n = int(input())
    new_lists = []
    count = 0

    for t in range(n):
        new_lists.append(list(map(int, input().split())))
        print(new_lists)
    print(new_lists)

    for i in range(n):
        for j in range(n):
            if new_lists[j][i] == 1:
                for d in range(j+1, n):
                    if new_lists[d][i] == 1 or new_lists[d][i] == 0:
                        break
                    elif new_lists[d][i] == 2:
                        count += 1

    print(f'#{T} {count}')

    # 뒤에 2가 몇개가 나오던 상관없이 2만 나오면 계속 더해지는 중이였음
    # 카운트 한번 되면 벗어나게 만들어야한다. 어떻게?
