# https://wayhome25.github.io/cs/2017/04/03/cs-03/

# from functools import reduce
#
# # 문제1. 전통적으로 최대값 구하기
# def maximum(li):
#     default = 0
#     for e in li:
#         if default < e:
#             default = e
#     return default
# maximum(li)
#
# # 문제1. reduce 활용하여 최대값 구하기
# reduce(lambda a,b: a if a > b else b ,li)



# def next_permutation(s):
#   for i in reversed(range(len(s))):
#     if s[i] > s[i-1]:
#       break
#   else:
#     return []
#   i -= 1
#   for j in reversed(range(i + 1, len(s))):
#     if s[j] > s[i]: break
#   t = s[i]
#   s[i] = s[j]
#   s[j] = t
#   s[i + 1:] = reversed(s[i + 1:])
#   return s
#
# print(next_permutation([1,2,3]))

# the largest index where A[i] < A[i + 1]
# -1 if there is no such i where A[i] < A[i + 1]


#
# def get_split_index(A):
#     i = len(A) - 1
#     while i > 0:
#         if A[i] < A[i - 1]:
#             i -= 1
#         else:
#             break
#     return i - 1
#
#
# def get_change_index(A, i):
#     j = len(A) - 1
#     while j >= i:
#         if A[j] > A[i]:
#             break
#         else:
#             j -= 1
#     return j
#
#
# def swap(A, i, j):
#     A[i], A[j] = (A[j], A[i])
#
#
# # reverse A[start:]
# def reverse(A, start):
#     left = start
#     right = len(A) - 1
#     while left < right:
#         swap(A, left, right)
#         left += 1
#         right -= 1
#
#
# def next_permutation(A):
#     split_index = get_split_index(A)
#     # the Array is sorted in descreased order
#     if split_index == -1:
#         reverse(A, 0)
#     else:
#         change_index = get_change_index(A, split_index)
#         swap(A, split_index, change_index)
#         reverse(A, split_index + 1)
#
#
#
#
# for i in range(30):
#     next_permutation(A)
#     print(A)

A = [1, 2, 3, 4]

def next_permutation(s):

    i = len(s) - 1
    while i > 0:
        if s[i] < s[i -1]:
            i -= 1
        else:
            break
    i -= 1

    if i == -1:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    else:
        j = len(s) - 1
        while j >= 1:
            if s[j] > s[i]:
                break
            else:
                j-=1
        s[i], s[j] = s[j], s[i]
        left = i+1
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

for _ in range(23):
    next_permutation(A) # [1, 3, 2]
    print(A)