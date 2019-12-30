'''

[[s1,e1],[s2,e2],...] (si < ei)
'''


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 가장 빨리 끝나는 값을 시작점으로 한다.
        # 때문에 sort한 리스트에서 진행한다

        newintervals = []
        for x, y in intervals:
            newintervals.append([y, x])

        newintervals.sort()

        st = newintervals[0][0]
        ans = 0
        for nxt in newintervals[1:]:
            if st <= nxt[1]:
                print(st, nxt[1])
                st = nxt[0]
                ans += 1
        print(ans)
        # return ans