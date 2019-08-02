'''

n개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

1 <= T <= 50
5 <= N <= 1000
1 <= aj <= 10000000
'''

def my_max(arr):
    temp = arr[0] # 리스트로 받은 것중에서 0인덱스를 기준으로
    for i in range(1, len(arr)): # 그다음 인덱스부터 끝까지
        if temp < arr[i]: # 만약 다음 인덱스가 더 크다면,
            temp = arr[i] # 다음인덱스를 temp값으로 둔다.
    return temp

def my_min(arr): # min도 마찬가지
    temp = arr[0]
    for i in range(1, len(arr)):
        if temp > arr[i]:
            temp = arr[i]
    return temp


for T in range(int(input())):
    N = int(input())
    aj = list(map(int, input().split()))
    result =  my_max(aj) - my_min(aj)
    print('#{} {}'.format(T+1, result))