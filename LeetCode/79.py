ans = False
class Solution(object):
    def exist(self, board, word):
        global ans
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 6
        def DFS(y, x, getlen):
            if getlen == wordlen:
                return True  # 끝까지 찾았을때 True를 반환
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                iy, ix = dy+y, dx+x
                if 0 <= iy < N and 0 <= ix < M and board[iy][ix] == word[getlen]:
                    board[iy][ix] = '-'
                    ans = DFS(iy, ix, getlen+1)
                    if ans:  # 반환된 ans가 True라면,
                        return True  # Root까지 True를 끌어올리면서 재귀를 빠져나간다.
                    # 반환된 ans가 False라면, 다시 visited했던 부분을 바꿔준다.
                    board[iy][ix] = word[getlen]
            return False  # 찾지못하면, False를 반환

        N = len(board)
        M = len(board[0])
        wordlen = len(word)
        for y in range(N):
            for x in range(M):
                if board[y][x] == word[0]:
                    board[y][x] = '-'
                    ans = DFS(y, x, 1)
                    board[y][x] = word[0]
                    if ans:
                        return True
        return False


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 6
        def DFS(y, x, getlen):
            if getlen == wordlen:
                return True
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                iy, ix = dy+y, dx+x
                if 0 <= iy < N and 0 <= ix < M and board[iy][ix] == word[getlen]:
                    board[iy][ix] = '-'
                    ans = DFS(iy, ix, getlen+1)
                    if ans:
                        return True
                    board[iy][ix] = word[getlen]
            return False

        N = len(board)
        M = len(board[0])
        wordlen = len(word)
        for y in range(N):
            for x in range(M):
                if board[y][x] == word[0]:
                    board[y][x] = '-'
                    ans = DFS(y, x, 1)
                    board[y][x] = word[0]
                    if ans:
                        return True
        return False
