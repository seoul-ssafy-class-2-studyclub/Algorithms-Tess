class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # 새로운 곳에 있는 걸 기준으로 수정한다.
        def solve(y, x, newarr):
            cnt = 0

            for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                iy = dy + y
                ix = dx + x
                if 0 <= iy < N and 0 <= ix < M and board[iy][ix] == 1:
                    cnt += 1
            print(cnt)
            if cnt == 1:
                newarr[y][x] = 0
                return newarr

            if cnt == 2:
                return newarr

            if cnt == 3:
                newarr[y][x] = 1
                return newarr

            if cnt > 4:
                newarr[y][x] = 0
                return newarr

        N = len(board)
        M = len(board[0])

        newarr = [i[:] for i in board]

        for y in range(N):
            for x in range(M):
                newarr = solve(y, x, newarr)

        newarr = [i[:] for i in newarr]
        board = newarr
        print(board)
        return board

# class Solution:
#     def gameOfLife(self, board: List[List[int]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         # Neighbors array to find 8 neighboring cells for a given cell
#         neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

#         rows = len(board)
#         cols = len(board[0])

#         # Iterate through board cell by cell.
#         for row in range(rows):
#             for col in range(cols):

#                 # For each cell count the number of live neighbors.
#                 live_neighbors = 0
#                 for neighbor in neighbors:

#                     # row and column of the neighboring cell
#                     r = (row + neighbor[0])
#                     c = (col + neighbor[1])

#                     # Check the validity of the neighboring cell and if it was originally a live cell.
#                     if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
#                         live_neighbors += 1

#                 # Rule 1 or Rule 3
#                 if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
#                     # -1 signifies the cell is now dead but originally was live.
#                     board[row][col] = -1
#                 # Rule 4
#                 if board[row][col] == 0 and live_neighbors == 3:
#                     # 2 signifies the cell is now live but was originally dead.
#                     board[row][col] = 2

#         # Get the final representation for the newly updated board.
#         for row in range(rows):
#             for col in range(cols):
#                 if board[row][col] > 0:
#                     board[row][col] = 1
#                 else:
#                     board[row][col] = 0