class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        q = []
        q.append((sr, sc))
        col, row = len(image), len(image[0])
        currentColor = image[sr][sc]
        '''
        [[0,0,0],
        [0,1,1]]
        같은 컬러로 newColor가 들어오는 경우가 존재한다.
        '''
        if currentColor == newColor:  # 같은 경우 바로 리턴하도록 설정하면 visit가 필요없어진다.
            return image

        image[sr][sc] = newColor
        while q:  # bfs가 더 빠른가?
            sr, sc = q.pop(0)
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                iy = dy + sr
                ix = dx + sc
                if 0 <= iy < col and 0 <= ix < row and image[iy][ix] == currentColor:
                    image[iy][ix] = newColor
                    q.append((iy, ix))
        return image
# Runtime: 56 ms, faster than 95.04% of Python online submissions for Flood Fill.
# Memory Usage: 11.7 MB, less than 90.91% of Python online submissions for Flood Fill.













class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        '''
        [[1,1,1],
        [1,1,0],
        [1,0,1]]
        sr = 1, sc = 1, newColor = 2
        (1, 1) 
        row col

        [[2,2,2],
        [2,2,0],
        [2,0,1]]


        # bfs로 색칠하기네
        sr sc가 0부터 시작이니까 인덱스도 0부터 겠네
        '''

        q = []
        q.append((sr, sc))
        col = len(image)
        row = len(image[0])
        print(col, row)
        print(sr, sc)
        currentColor = image[sr][sc]
        image[sr][sc] = newColor
        print(image)
        print(newColor)
        visit = [[False] * row for _ in range(col)]
        visit[sr][sc] = True
        while q:
            sr, sc = q.pop(0)
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                iy = dy + sr
                ix = dx + sc
                if 0 <= iy < col and 0 <= ix < row and image[iy][ix] == currentColor and visit[iy][ix] == False:
                    image[iy][ix] = newColor
                    visit[iy][ix] = True
                    q.append((iy, ix))
        return image

        '''
        [[0,0,0],
        [0,1,1]]
        같은 컬러로 newColor가 들어오는 경우가 존재한다.
        '''