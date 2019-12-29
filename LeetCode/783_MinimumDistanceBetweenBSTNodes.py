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