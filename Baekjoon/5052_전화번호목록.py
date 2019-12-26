'''
일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.

NO
YES
'''

import sys
sys.stdin = open('5052.txt', 'r')



## 접두어가 겹치면 안된다
'''
97625999이 
97625999000의 접두어 이므로 NO가 된다.

앞에나온 모든 정보를 가지고
새로나온 정보에 대해서 check 한다.
'''


import sys
input = sys.stdin.readline

# 모두 받은 후 처리 필
# 답을 찾으면 바로 끝내버린
def solve():
    st = phone[0]
    for ph in phone[1:]:
        if st in ph:
            return 'NO'
        else:
            st = ph # st를 현재문자열로 변경해준다.
    return 'YES'

t = int(input())
for _ in range(t):
    n = int(input())
    phone = []
    for i in range(n):
        data = input().rstrip()
        phone.append(data)
    phone.sort()
    print(solve())


# import sys
# input = sys.stdin.readline
#
#
# def solve(contacts):
#     contacts.sort()
#     st = contacts[0]
#     for contact in contacts[1:]:
#         if st in contact:
#             return "NO"
#         else:
#             st = contact
#
#     return "YES"
#
#
# for i in range(int(input())):
#
#     n = int(input())
#     contacts = []
#
#     for j in range(n):
#         contacts.append(input().rstrip())
#
#     ans = solve(contacts)
#     print(ans)


## 받으면서 하나씩 비교하니까 시간초과가 뜬다.
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     phone = dict()
#     flag = True
#     ans = 'YES'
#     s = 0
#     for i in range(n):
#
#         data = input()
#         if flag == True:
#             phone[data] = len(data)
#             if s == 0:
#                 s = 1
#                 continue
#
#             if s == 1:
#                 for key, val in phone.items():
#                     if key != data:
#                         if key == data[:val]:
#                             ans = 'NO'
#                             flag = False
#                             break
#
#     print(ans)


# for _ in range(t):
#     n = int(input())
#
#     save = []
#     ans = 'YES'
#
#     for i in range(n):
#         data = input()
#         save.append(data)
#
#     check = [False]*n
#     i = 0
#     while save:
#
#         cur = save[i]
#         check[i] = True
#
#         num = len(cur)
#         nxt = save[i+1]
#
#         print(cur, nxt)
#         while cur != nxt[i+1][:num] and i+1 < n and check[i] == True:
#             print(cur, nxt)
#             save.append(nxt) # 같지않으면 다시 저장
#             i += 1
#
#         if i == n:
#             break
#
#     print(save)