class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        origin = [0, 0]
        for m in moves:
            if m == 'R':
                origin[1] += 1
            if m == 'L':
                origin[1] -= 1
            if m == 'U':
                origin[0] += 1
            if m == 'D':
                origin[0] -= 1
        return True if origin[0] == origin[1] == 0 else False


class Solution(object):
    def judgeCircle(self, moves):
        R = L = U = D = 0
        for m in moves:
            if m == 'R':
                R += 1
            if m == 'L':
                L += 1
            if m == 'U':
                U += 1
            if m == 'D':
                D += 1
        return True if R == L and U == D else False