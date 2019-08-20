import sys
sys.stdin = open('5986.py', 'r')

def is_prime(num):
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        # 여기서 i가 소수인지 알 수 있으면 더 빠르게 판별 가능.
        # is_prime(i)로 체크하면 n팩토리얼의 복잡도를 가진다.
        if num % i == 0:
            return False
        i += 1
    return True

#소수구하는 방법 : 에라토스테레스 체

False, True
소수를 주어진 구간내에서
소수인지 아닌지 걸러내는 방법

소수가 아닌 수 = 합성수
합성수 = 소수 * 소수  -> 소인수분해

소수의 배수를 구하면 합성수


소수가 아니면 전부 False vytl

11길이라면

[0 1 2] 3은 이미 있으므로              8개
[False False True] + [True]*구하고자 하는 구간만큼 곱한다


0  1 2 3 4 5 6 7 ...
[F F T T T T T T ...] # 안걸러진 애들이 점점 소수로 판단되면서 반복되는 과정

if True? -> 새로운 리스트에 index를 넣는다.
    for (2, len, i) 4/6/8 # 2는 소수이므로 빼고 해야한다.




