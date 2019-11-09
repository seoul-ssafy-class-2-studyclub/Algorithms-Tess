import sys
sys.stdin = open('input.txt', 'r')

'''
스택에 뒤에 두개 이상 같은 모양이 쌓이면 사라짐
2차원 배열 board
인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves
크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 

board 
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

moves
[1,5,3,5,1,2,1,4]

result 
4
'''
# from pprint import pprint
# import collections
# def solution(board, moves):
#     # pprint(board)
#     boardx = len(board)
#     moves = collections.deque(map(int, moves))
#     # NxN 이다
#     # moves의 앞에서 부터 빼면서
#     # moves의 번호에 맞춰서 (인덱스를 -1씩 해가며?)
#     # stack에 해 1~100에 해당하는 인형을 추가한다.
#     mystack = [0]
#     answer = 0
#     while moves:
#         pos = moves.popleft()
#         for y in range(boardx):#0~5
#             if board[y][pos-1] != 0:
#
#                 # 만약 mystack에 마지막에 쌓인게 현재 크레인이 가지고 오는거랑 같다면,
#                 # mystack에 쌓인걸 없애고, 크레인이 가지고오는것도 없앤 후
#                 # answer에 +2를 한다.
#                 if mystack[-1] == board[y][pos - 1]:
#                     board[y][pos - 1] = 0
#                     answer += 2
#                     mystack.pop()
#                     break
#                 # 그렇지 않은 경우
#                 else:
#                     mystack.append(board[y][pos - 1])
#                     board[y][pos - 1] = 0
#                     break
#     return answer
#
#
# board = []
# for b in range(5):
#     d = list(map(int, input().split(',')))
#     board.append(d)
# moves = list(map(int, input().split(',')))
#
# solution(board, moves)

# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
#



#
# def solution(s):
#     num, idx = [0] * 501, [0] * 501
#     visited = [False] * 100001
#     stack = []
#     numb, leng, now = '', 0, 1
#     for letter in s:
#         if numb and letter == ',' :
#             stack.append(int(numb))
#             numb = ''
#             leng += 1
#         elif numb and letter == '}' :
#             stack.append(int(numb))
#             leng, numb = leng+1, ''
#             num[now], stack = stack[:], []
#             idx[leng] = now
#             leng, now = 0, now+1
#         elif letter.isdigit():
#             numb += letter
#     answer = []
#     for i in range(1, 501):
#         if idx[i] != 0:
#             for j in num[idx[i]]:
#                 if visited[j] == False:
#                     answer.append(j)
#                     visited[j] = True
#                     break
#     return answer
#
# solution(s)
# #
# '''
# n개의 요소를 가진 튜플을 n-튜플(n-tuple)
# (a1, a2, a3, ..., an)
#
# 중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
#
# 원소에 정해진 순서가 있으며,
# 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
# # 같게 생겼냐 안같게 생겼냐 -> str화 해서 확인
#
# 튜플의 원소 개수는 유한합니다.
#
#
#
# # 데이터를 받아서,
# {지우고 } 지우고
# replace한다.
# ,을 기준으로 나눈 후
# 숫자는 모두 int로 만들고
# set 처리해서
# 숫자만 남겨서
# list에 넣는다
#
# '''
#
# solution(input())
#



'''

 프로도 에게 전달하려고 합니다. 
 이 때 개인정보 보호을 위해 사용자 아이디 중 일부 문자를 '*' 문자로 가려서 전달했습니다. 
 가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고
  아이디 당 최소 하나 이상의 '*' 문자를 사용하였습니다.




'''


#
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]
# # 경우의 수를 구한다
# # 가능한 경우는 bannded_id에 저장한다
# #bannded_id가 count하는게 될 것
# import collections
# import itertools
#
# fin = False
# def solution(user_id, banned_id):
#     global fin
#     mydict = {}
#     user_id = collections.deque(user_id)
#     for i in banned_id:
#         mydict[i] = 0
#     possible = []
#     mynewdict2 = {}
#     for i in user_id:
#         mynewdict2[i] = []
#     # 하나씩 체크하자
#     while user_id:
#         check = user_id.popleft()
#         for i in range(len(banned_id)):
#             firstcnt = 0
#             secondcnt = 0
#
#             for idx in range(len(check)):
#                 if len(check) == len(banned_id[i]) and check[idx] == banned_id[i][idx]:
#                     firstcnt += 1
#
#                 if len(check) == len(banned_id[i]) and check[idx] != banned_id[i][idx] and banned_id[i][idx] == '*':
#                     secondcnt += 1
#             if (firstcnt+secondcnt) == len(check):
#                 mydict[banned_id[i]] += 1
#                 mynewdict2[check].append(i)
#                 if check not in possible:
#                     possible.append(check)
#
#     def solve(idx=0, stop=0):
#         global fin
#         if stop == len(banned_id):
#             fin = True
#             return True
#         if idx == len(banned_id):
#             return False
#         for ban in mynewdict2[mylist[idx]]:
#             if not vis[ban]:
#                 vis[ban] = True
#                 solve(idx + 1, stop + 1)
#                 vis[ban] = False
#
#     vis = [0] * len(banned_id)
#     answer = 0
#     mycombi = list(itertools.combinations(possible, len(banned_id)))
#     for mylist in mycombi:
#         fin = False
#         solve()
#         if fin:
#             answer += 1
#     return answer
# solution(user_id, banned_id)




'''
호텔에는 방이 총 k개
각각의 방은 1번부터 k번까지 번호로 구분

한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
고객은 투숙하기 원하는 방 번호를 제출합니다.
고객이 원하는 방이 비어 있다면 즉시 배정합니다.

고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 
가장 번호가 작은 방을 배정합니다.


'''
#
# [1,3,4,2,5,6]
# k = 10
# room_number = [1,3,4,1,3,1]
#
#
# from collections import deque
#
# def solution(k, room_number):
#     counting = [0] + [0]*k
#     order = []
#     room_number = deque(room_number)
#     while room_number:
#         customer = room_number.popleft()
#         if counting[customer] == 0:
#             counting[customer] = 1
#             order.append(customer)
#
#         elif counting[customer] == 1:
#             for idx in range(customer+1, len(counting)+1):
#                 if counting[idx] == 0:
#                     order.append(idx)
#                     counting[idx] = 1
#                     break
#     print(order)
#     return order
#
# solution(k, room_number)
# # print(order)

def solution(k, room_number):
   answer = []
   linking = {i:0 for i in range(k+1)}
   for i in room_number:
       currnt_idx = i
       while linking[currnt_idx] != 0 :
           currnt_idx = linking[currnt_idx]
       linking[currnt_idx] = currnt_idx+1
       currnt_room = room_list[currnt_idx]
       answer.append(currnt_room)
   return answer