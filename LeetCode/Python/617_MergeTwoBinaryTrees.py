'''
a bit confused because leetcode problem's input is different from Baekjoon
decided to note the description for such problems like this

what is a binary tree(이진트리)?
it's a tree data structure that has the maximum of two children.
the two children are called as an right node and a left node.

각각의 노드가 최대 두 개의 자식 노드를 가지는 트리 자료 구조로,
자식 노드를 각각 왼쪽 자식 노드와 오른쪽 자식 노드라고 한다.


새로운 Tree를 만들지 않고
그냥 recursion 하면서 t1에다 val이나 reference를 update 하는 방식으로 구현
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        else:
            t1 = t1 or t2
        return t1
