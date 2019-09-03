import sys
sys.stdin = open('5110.txt', 'r')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        HeadNode = Node("HEAD")
        self.head = HeadNode
        self.tail = HeadNode
        self.NumOfData = 0

    def insert(self, data):
        insertNode = Node(data)
        self.tail.next = insertNode
        self.tail = insertNode
        self.NumOfData += 1

    # def delete(self):
    #     if self.NumOfData == 0:
    #         print("List is empty!")
    #         return False
    #     elif self.NumOfData == 1:
    #         delete_node = self.head.next
    #         self.head.next = None
    #         self.tail = self.head
    #         self.NumOfData -= 1
    #         print("리스트에서", delete_node.data, "데이터를 삭제하였습니다.")
    #         return delete_node.data
    #     else:
    #         delete_node = self.head.next
    #         self.head.next = self.head.next.next
    #         self.NumOfData -= 1
    #         print("리스트에서 ", delete_node.data, "데이터를 삭제하였습니다.")
    #         return delete_node.data

    def search(self, data, other):
        check = self.head
        for i in range(self.NumOfData):
            if check.next.data == data:
                print(data, "데이터는", i + 1, "번째에 있습니다.")
                return None
            check = check.next
        print(data, "데이터는 리스트에 없습니다.")
        return None

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M - 1):
        new_numbers = list(map(int, input().split()))
        first_num = new_numbers[0]

        for i in range(len(numbers)):
            if first_num < numbers[i]:
                numbers[i:0] = new_numbers
                break
        else:
            numbers += new_numbers

    numbers = numbers[-10:]
    result = ' '.join(list(map(str, reversed(numbers))))
    print('#{} {}'.format(tc, result))

    # def listNum(self):
    #     print("현재 리스트에는", self.NumOfData, "개의 요소가 있습니다.")
    #     return self.NumOfData

    # def printList(self):
    #     current = self.head
    #     if self.NumOfData == 0:
    #         print("List is empty!")
    #         return None
    #     print("HEAD::", end='')
    #     for i in range(self.NumOfData - 1):
    #         print(current.next.data, "->", end='')
    #         current = current.next
    #     print(current.next.data)
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    n = N
    for _ in range(M-1):
        new_numbers = list(map(int, input().split()))
        first_num = new_numbers[0]


        for i in range(n):
            if first_num < numbers[i]:
                numbers = numbers[:i] + new_numbers + numbers[i:]
                break
        else:
            numbers += new_numbers
        n += N
    numbers = numbers[-10:]
    result = ' '.join(list(map(str, reversed(numbers))))
    print('#{} {}'.format(tc, result))
'''


#
# ## 병합정렬로 수정
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     all_nums = []
#     for m in range(M):
#         random_nums = list(map(int, input().split()))
#         all_nums.append(random_nums)
#     res = []
#     res.extend(all_nums[0])
#     print(res)
#     for idx1 in range(len(all_nums)-1):
#         for idx2 in range(idx1+1, len(all_nums)):
#             if idx1 == 0:
#                 if max(all_nums[idx1]) > all_nums[idx2][0]:
#                     idx3 = all_nums[idx1].index(max(all_nums[idx1]))
#                     for idx4 in range(idx3, idx3+N):
#                         for n in range(N):
#                             res.insert(idx4, all_nums[idx2][n])
#             else:
#                 if max(res) > all_nums[idx2][0]:
#                     idx3 = res.index(max(res))
#                     for idx4 in range(idx3, idx3+N):
#                         for n in range(N):
#                             res.insert(idx4, all_nums[idx2][n])
#                 else:
#                     res.extend(all_nums[idx2])
#
#     print(list(sorted(res)))