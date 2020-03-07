class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0: return True
        flowerbed = [0]+flowerbed+[0] # arr를 원하는 방향으로 수정하기
        for idx in range(1, len(flowerbed)-1):
            if flowerbed[idx] == 0 and flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0:
                flowerbed[idx] = 1
                n -= 1
            if n == 0:
                return True
        return False