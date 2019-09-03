import sys
sys.stdin = open('5099.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = []
    for name, num in enumerate(cheese, start=1):
        pizza.append((name, num))

    cooking = pizza[:N]
    pizza = pizza[N:]
    while len(cooking) != 1:
        name, Ci = cooking.pop(0)
        C = Ci//2
        if C == 0:
            if len(pizza) >= 1:
                temp_name, temp_Ci = pizza.pop(0)
                cooking.append((temp_name, temp_Ci))

        elif C != 0:
            cooking.append((name, C))

    for name, num in cooking:
        print(f'#{tc} {name}')