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

#소수구하는 방법 : 아리스토텔레스
