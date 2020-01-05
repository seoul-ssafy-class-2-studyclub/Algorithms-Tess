# Intuition
#
# For each index S[i],
# let's try to find the distance
# to the next character C going left, and going right.
# The answer is the minimum of these two values.
#
# Algorithm
#
# When going left to right,
# we'll remember the index prev of the last character C we've seen.
# Then the answer is i - prev.
#
# When going right to left,
# we'll remember the index prev of the last character C we've seen.
# Then the answer is prev - i.
#
# We take the minimum of these two answers to create our final answer.
class Solution(object):
    def shortestToChar(self, S, C):
        # C를 만나면 뒤로가면서 cnt를 늘려주면서 채워줌
        # prev값에 c의 인덱스
        ans = [1e9]*len(S)
        for idx, val in enumerate(S):
            if val == C:
                oidx = idx
                flag = True
                cnt = 0
                while flag:
                    idx -= 1
                    if 0 <= idx < len(S):
                        if S[idx] != C:
                            cnt += 1
                            if ans[idx] > cnt:
                                ans[idx] = cnt
                            else:
                                flag = False
                                break
                        else:
                            flag = False
                            break
                    else:
                        break
                flag = True
                idx = oidx
                cnt = 0
                while flag:
                    idx += 1
                    if 0 <= idx < len(S):
                        if S[idx] != C:
                            cnt += 1
                            ans[idx] = cnt
                        else:
                            flag = False
                            break
                    else:
                        break
                ans[oidx] = 0
        return ans
# Runtime: 24 ms, faster than 88.16% of Python online submissions for Shortest Distance to a Character.
# Memory Usage: 11.7 MB, less than 75.00% of Python online submissions for Shortest Distance to a Character.


#O(2N)
class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf') # 1e9 보다 빠르다.
        ans = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            ans += [i - prev] #

        prev = float('inf') # 뒤에서 C가 없는 경우를 대비해서 inf로 해야한다.
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

# Runtime: 16 ms, faster than 100.00% of Python online submissions for Shortest Distance to a Character.
# Memory Usage: 11.8 MB, less than 50.00% of Python online submissions for Shortest Distance to a Character.

class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
# Runtime: 24 ms, faster than 88.16% of Python online submissions for Shortest Distance to a Character.
# Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Shortest Distance to a Character.


# class Solution:
#     def shortestToChar(self, S, C):
#         c_pos = [i for i in range(len(S)) if S[i]==C]
#         return [min(abs(i-c) for c in c_pos) for i in range(len(S))]


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        Cidx = []
        for idx, val in enumerate(S):
            if val == C:
                Cidx.append((idx))
        # 가장 작은 distance
        # 뺐을때 가장 작은 값
        ans = [0]*len(S)
        for idx, Sval in enumerate(S):
            mymin = 1e9
            temp = 0
            if Sval != C:
                for Cval in Cidx:
                    temp = abs(Cval - idx)
                    if mymin > temp:
                        mymin = temp
                ans[idx] = mymin
        return ans

# Runtime: 52 ms, faster than 26.64% of Python online submissions for Shortest Distance to a Character.
# Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Shortest Distance to a Character.


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ans = [0] * len(S)
        Cidx = []
        children = []
        for idx, val in enumerate(S):
            if val == C:
                Cidx += [idx]
            if val != C:
                children += [idx]

        while children:
            orichild = children.pop(0)
            orichildnum = orichild
            ix = orichild
            flag = 0
            while flag == 0:
                ix = orichild + 1
                if 0 <= ix < len(S) and flag == 0:
                    if S[ix] == C:
                        ans[orichildnum] = abs(ix - orichildnum)
                        flag = 1
                        break
                    else:
                        orichild = ix
                else:
                    flag = 1
                    break

            orichild = orichildnum
            ix = orichild
            flag = 0
            while flag == 0:
                ix = abs(orichild - 1)
                # 3-1 2
                if 0 <= ix < len(S) and flag == 0:
                    if S[ix] == C:
                        temp = abs(abs(ix) - orichildnum)
                        if temp < ans[orichildnum]:
                            ans[orichildnum] = temp
                            flag = 1
                            break
                        else:
                            flag = 1
                            break
                    else:
                        orichild = ix
                else:
                    flag = 1
                    break
        return ans