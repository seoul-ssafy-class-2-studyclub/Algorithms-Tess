# 언뜻보면 완탐 가능하겠는데? 싶다가도
# DP로 접근했어야 하는 문제

class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0: return 0  # 빈리스트인경우
        # [["0"]] => 0
        # [["1"]] => 1
        # if len(matrix) == 1 and matrix[]
        N = len(matrix)
        M = len(matrix[0])
        mymax = -1e9
        for y in range(N):
            for x in range(M):
                if matrix[y][x] == "0":
                    mymax = 0
                    continue
                elif matrix[y][x] == "1":  # DP의 시작
                    mymin = 1e9
                    for dy, dx in [(0, -1), (1, 0), (1, -1)]:
                        iy = dy + y
                        ix = dx + x
                        if 0 <= iy < N and 0 <= ix < M:
                            if mymin > matrix[iy][ix]:
                                mymin = matrix[iy][ix]
                        print(mymin)
                        if y == 0 or x == 0:
                            matrix[y][x] = 0

                    matrix[y][x] = mymin + 1
                    if mymax < matrix[y][x]:
                        mymax = matrix[y][x]

        return mymax



# class Solution(object):
#     def maximalSquare(self, matrix):
#         if not matrix: return 0
#         m = len(matrix)
#         n = len(matrix[0])
#         max_len = 0
#
#         for i in range(m):
#             matrix[i][0] = int(matrix[i][0])
#             max_len = max(max_len, matrix[i][0])
#         for j in range(1, n):
#             matrix[0][j] = int(matrix[0][j])
#             max_len = max(max_len, matrix[0][j])
#
#         for i in range(1,m):
#             for j in range(1,n):
#                 if int(matrix[i][j]) != 0:
#                     matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])+1
#                 else:
#                     matrix[i][j] = 0
#                 max_len = max(max_len, matrix[i][j])
#
#         return max_len*max_len
#
