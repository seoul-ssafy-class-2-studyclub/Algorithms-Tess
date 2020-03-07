class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):

        # 1을 설명해보면, 그렇지 않은 경우 rec1의 top-right부분이 rec2의 bottom-left부분을 침범하기때문이다.
        # 뭐든 true가 되는 경우 겹치지 않은 것인데, 결과는 겹치지 않으면 false를 출력해야하기 때문에 다음과 같이 리턴
        # 뭐든 false가 되는 경우 겹치는 것, 그래서 true를 리턴한다.
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top