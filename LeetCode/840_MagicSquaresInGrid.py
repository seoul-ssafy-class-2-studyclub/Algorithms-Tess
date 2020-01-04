
class Solution(object):
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])

        def magic(a ,b ,c ,d ,e ,f ,g ,h ,i):
            return (sorted([a ,b ,c ,d ,e ,f ,g ,h ,i]) == range(1, 10) and
                    ( a + b +c == d+ e + f == g + h + i == a + d + g ==
                     b + e + h == c + f + i == a + e + i == c + e + g == 15))


        ans = 0
        for r in range(R - 2):
            for c in range(C - 2):
                if grid[r + 1][c + 1] != 5: continue  # optional skip
                # 3x3이 같아야 한다는 건 조건이니까 이런식으로 함수를 보내서 확인하는게
                # for문을 도는것 보다 복잡하지 않고 좋네..!
                if magic(grid[r][c], grid[r][c + 1], grid[r][c + 2],
                         grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                         grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2]):
                    ans += 1
        return ans

