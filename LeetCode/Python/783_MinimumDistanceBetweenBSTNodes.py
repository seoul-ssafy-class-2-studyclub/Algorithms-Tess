class Solution(object):
    def minDiffInBST(self, root):
        mymin = 1e9
        prev = None
        curr = root
        start = []
        while curr or start:
            while curr:
                start.append(curr)
                curr = curr.left

            curr = start.pop()

            if prev != None:
                mymin = min(mymin, abs(curr.val - prev.val))

            prev = curr
            curr = curr.right

        return mymin


### [4,2,6,1,3,null,null] 인 경우
class Solution(object):
    def minDiffInBST(self, root):
        mymin = 1e9
        prev = None
        curr = root
        start = []
        while curr or start:  # curr 혹은 start가 비어있지 않다면,

            while curr:  # curr의 왼쪽에서 null을 만날때까지 실행하는데,
                start.append(curr)  # start에 curr을 넣고,
                curr = curr.left  # curr의 왼쪽 노드들을 순회할 수 있도록 추가 => [4, 2, 1]이 추가 된다.

            curr = start.pop()  # pop을해서 마지막으로 추가된 => 1을 방문한다.

            if prev != None:  # prev가 None이 아니라면, 비교할 수 있다는 뜻이므로
                mymin = min(mymin, abs(curr.val - prev.val))

            prev = curr  # => 1
            curr = curr.right  # 1은 오른쪽 자식이 없으므로 => null

        return mymin