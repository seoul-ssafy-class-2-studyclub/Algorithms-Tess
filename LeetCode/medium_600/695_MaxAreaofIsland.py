def maxAreaOfIsland(grid):
    ans = 0
    M, N = len(grid), len(grid[0])
    stack = []
    for y in range(M):
        for x in range(N):
            if grid[y][x] == 1:
                stack.append((y,x))
                grid[y][x] = 0
                st = 1
                while stack:
                    y, x = stack.pop()
                    for dy, dx in [(0,1), (0,-1), (1, 0), (-1,0)]:
                        iy = y + dy
                        ix = x + dx
                        if 0 <= iy < M and 0 <= ix < N and grid[iy][ix] == 1:
                            grid[iy][ix] = 0
                            stack.append((iy, ix))
                            st += 1
                if st > ans:
                    ans = st
    return ans


# 굳이 visited를 할 필요가 없었다. 
# 바로 빨라졌음!
print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],[0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))

