# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next  # 1의 다음인 2 // 2의 다음인 3
            curr_node.next = prev_node  # 1의 다음은 None으로 변경 (reverse) // 1은 2의 다음으로 변경된다.
            prev_node = curr_node  # 1은 변경될 prev로 // 2는 변경된 prev로
            curr_node = next_node  # 2는 현재가 된다 // 3은 현재가 된다.
        head = prev_node
        return head
