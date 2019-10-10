import sys
sys.stdin = open('1991.txt', 'r')

'''
전위 순회(preorder traversal), 
현-왼-오

중위 순회(inorder traversal), 
왼-현-오

후위 순회(postorder traversal)
왼-오-현

ABDCEFG
DBAECFG
DBEGFCA


https://onestep.tistory.com/42
'''


'''
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 
자식 노드가 없는 경우에는 .으로 표현된다.
'''


import sys
input = sys.stdin.readline

def preordertraversal(node):
    global preres
    preres += node
    if tree[node][0] != '.':
        preordertraversal(tree[node][0])

    if tree[node][1] != '.':
        preordertraversal(tree[node][1])


def inordertraversal(node):
    global inorderres
    if tree[node][0] != '.':
        inordertraversal(tree[node][0])

    inorderres += node
    if tree[node][1] != '.':
        inordertraversal(tree[node][1])

def postordertraversal(node):
    global postorder
    if tree[node][0] != '.':
        postordertraversal(tree[node][0])

    if tree[node][1] != '.':
        postordertraversal(tree[node][1])

    postorder += node

N = int(input())
tree = {}
for i in range(1, N+1):
    temp = input().split()
    if temp[2] == '.':
        tree[temp[0]] = [temp[1], '.']
    else:
        tree[temp[0]] = [temp[1],  temp[2]]

preres = ''
inorderres = ''
postorder = ''
preordertraversal('A')
inordertraversal('A')
postordertraversal('A')
print(preres)
print(inorderres)
print(postorder)

