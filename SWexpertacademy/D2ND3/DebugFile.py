# 부분 집합 알고리즘
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)



arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n): # 1<<n 부분 집합의 개수
    for j in range(n): # 원소의 수만큼 비트를 비교함
        if i&(1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=",")
    print()