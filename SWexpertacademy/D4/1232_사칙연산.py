import sys
sys.stdin = open('1232.txt', 'r')



# 이진트리다.
# L, R 리스트에 각각의 정보를 넣고,
# 단말노드(왼쪽, 오른쪽)을 현재노드(루트)에 맞게 연산을 해야하는데,

# 후위? 왼쪽->오른쪽->연산자에따라 왼쪽과 오른쪽을 다르게 연산해야한다.
# 단말노드가 나오면 return시키는 식으로 하기
def postorder_traverse(node):
    if Left[node] == 0:
        return tree[node]

    left = postorder_traverse(Left[node])
    right = postorder_traverse(Right[node])

    if tree[node] == "+":
        return left + right

    if tree[node] == "-":
        return left - right

    if tree[node] == "*":
        return left * right

    if tree[node] == "/":
        return left // right

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    Left = [0] * (N+1)
    Right = [0] * (N+1)

    for _ in range(N):
        inputData = list(map(str, input().split()))
        id = int(inputData[0])

        if len(inputData) > 2:
            tree[id] = inputData[1]
            Left[id] = int(inputData[2])
            Right[id] = int(inputData[3])
        else:
            tree[id] = int(inputData[1])
    print(f'#{tc} {postorder_traverse(1)}')



#
# '''
# 정점이 단순한 수이면 정점번호와 해당 양의 정수가 주어지고,
# 정점이 연산자이면 정점번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호가 차례대로 주어진다.
# '''
#
# # 이진트리다.
# # L, R 리스트에 각각의 정보를 넣고,
# # 단말노드(왼쪽, 오른쪽)을 현재노드(루트)에 맞게 연산을 해야하는데,
#
# # 후위? 왼쪽->오른쪽->연산자에따라 왼쪽과 오른쪽을 다르게 연산해야한다.
# # 단말노드가 나오면 return시키는 식으로 하기
# def postorder_traverse(node):
#     # global res
#
#     if Left[node] == 0:
#         # print(tree[node])
#         return tree[node]
#     # 1부터 시작해서 재귀결과를 가져온다.
#     # 왼
#     # 오
#     # 연산자(현재)
#
#     # else:
#     left = postorder_traverse(Left[node])
#     right = postorder_traverse(Right[node])
#     # print(left, right)
#     #  “+, -, *, /"
#     if tree[node] == "+":
#         return left + right
#
#     if tree[node] == "-":
#         return left - right
#
#     if tree[node] == "*":
#         return left * right
#
#     if tree[node] == "/":
#         return left // right
#
# for tc in range(1, 11):
#     N = int(input())
#     tree = [0] * (N+1)
#     Left = [0] * (N+1)
#     Right = [0] * (N+1)
#
#     for _ in range(N):
#         inputData = list(map(str, input().split()))
#         id = int(inputData[0])
#
#         # if 조건으로, 3 이상이면 left에, 4이상이면 right에
#         if len(inputData) > 2: # 중요!
#             tree[id] = inputData[1]
#             Left[id] = int(inputData[2])
#             Right[id] = int(inputData[3])
#         else:
#             tree[id] = int(inputData[1])
#     # print(res)
#
#     print(f'#{tc} {postorder_traverse(1)}')
