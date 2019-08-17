# A = list(map(int, input().split()))
#
# if 0 in A:
#     print(0)
# else:
#     print(1)

# A = int(input())
#
# if A < 0:
#     print(A)
#     print('minus')
# else:
#     print(A)

# height, weight = map(int, input().split())
#
# # weight+100-height = obesity
# res = weight+100-height
# print(res)
# if res > 0:
#     print('Obesity')

# A = int(input())
#
# total = 0
# for num in range(A+1):
#     total += num
# print(total)

# while True:
#     A = int(input())
#     if A < 0:
#         break
#     elif A%3 == 0:
#         print(A//3)
#     elif A%3 != 0:
#         continue

# A = int(input())
# for a in range(1, A+1):
#     print(a, end=' ')


# A = list(map(int, input().split()))
# odd = 0
# even = 0
# for a in A:
#     if a != 0:
#         if a%2 == 1:
#             odd += 1
#         elif a%2 == 0:
#             even += 1
#     elif a == 0:
#         break
# print('odd :', odd)
# print('even :', even)

# A = list(map(int, input().split()))
# cnt = 0
# for a in A:
#     if a%3 != 0:
#         if a%5 != 0:
#             cnt += 1
# print(cnt)

# A = int(input())
# cnt = 0
# for i in range(A, 101):
#     cnt += i
# print(cnt)

# A = list(map(int, input().split()))
# cnt3 = 0
# cnt5 = 0
# for a in A:
#     if a%3 == 0:
#         cnt3 += 1
#     if a%5 == 0:
#         cnt5 += 1
# print('Multiples of 3 :', cnt3)
# print('Multiples of 5 :', cnt5)

# for a in range(2, 7):
#     for i in range(5):
#         print(a+i, end=' ')
#     print()

# A, B = map(int, input().split())
# if B > A:
#     for b in range(A, B+1):
#         print(b, end=' ')
# elif B < A:
#     for a in range(B, A+1):
#         print(a, end=' ')

# A = int(input())
# cnt = 0
# for i in range(1, A+1):
#     if i%5 == 0:
#         cnt += i
# print(cnt)

# A = int(input())
# for i in range(1, 11):
#     print(A*i, end=' ')

# i, j = map(int, input().split())
# for ix in range(1, i+1):
#     for jy in range(1, j+1):
#         print(ix*jy, end=' ')
#     print()

# A = int(input())
# for i in range(1, 5):
#     for j in range(1,5):
#         print('({}, {})'.format(i, j), end=' ')
#     print()

# A, B = map(int, input().split())
# new = []
# for i in range(B, A+1):
#     new.append(i)
# newone = list(reversed(new))
#
#
# for n in range(1, 10):
#     for id in newone:
#         res = id*n
#         if res >= 10:
#             print('{1} * {2} = {0}'.format(res, id, n), end='   ')
#         elif res < 10:
#             print('{1} * {2} =  {0}'.format(res, id, n), end='   ')
#     print()


# A = int(input())
# total = 0
# cnt = 0
# for a in range(1, A+1):
#     if a%2 == 1:
#         total += a
#         cnt += 1
#         if cnt == 10:
#             print(cnt, total)

# A = int(input())
# for a in range(1, A+1):
#     print('*'*a)


# A = int(input())
# for i in range(1, 100):
#     res = i*A
#     print(res, end=' ')
#     if res%10 == 0:
#         break



###88 123 659 15 443 1 99 313 105 48
# def under100(arr):
#     new = [a for a in arr if a < 100]
#     temp = 0
#     for n in new:
#         if temp < n:
#             temp = n
#     return temp
#
#
# def over100(arr):
#     new = [a for a in arr if a >= 100]
#     temp = new[0]
#     for n in new:
#         if temp > n:
#             temp = n
#     return temp
#
# A = list(map(int, input().split()))
# print(under100(A), over100(A))

# A = int(input())
# for a in range(A, 0, -1):
#     print('*'*a)
# for a in range(1, A+1):
#     print('*'*a)


# A = int(input())
# for a in range(A, 0, -1):
#     if a == A:
#         print('*'*a)
#     if a < A:
          # 3-3=0 3-2=1 3-1=2
#         print(' ' * (A - a), end='')
#         print('*'*a)
# '''
# ***
#  **
#   *
# '''








