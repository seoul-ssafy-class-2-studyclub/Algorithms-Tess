class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        Y = len(grid)
        X = len(grid[0])
        rotten = []
        fresh = 0
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 2:
                    rotten += [(y, x)]
                if grid[y][x] == 1:
                    fresh += 1

        time = 0
        if not fresh and rotten or not fresh and not rotten: return time

        while rotten and fresh:  # 2만 있는 경우도 존재해서 fresh가 있고, 2가 있는 경우로 조건을 바꿔줘야 한다.
            time += 1
            for _ in range(len(rotten)):
                ry, rx = rotten.pop(0)
                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    iy, ix = dy + ry, dx + rx
                    if 0 <= iy < Y and 0 <= ix < X and grid[iy][ix] == 1:
                        grid[iy][ix] = 2
                        fresh -= 1
                        rotten += [(iy, ix)]
                        if fresh == 0:
                            return time
        if fresh != 0:
            return -1

# Runtime: 32 ms, faster than 92.52% of Python online submissions for Rotting Oranges.
# Memory Usage: 11.9 MB, less than 25.00% of Python online submissions for Rotting Oranges.