class Solution(object):
    def findJudge(self, N, trust):
        inDegree = [0] * (N + 1)
        outDegree = [0] * (N + 1)
        for t in trust:
            inDegree[t[1]] += 1
            outDegree[t[0]] += 1
        fin = []
        ans = []
        for idx in range(1, N + 1):
            if inDegree[idx] == (N - 1):
                fin += [idx]
            if idx in fin:
                if outDegree[idx] == 0:
                    ans += [idx]

        if len(ans) > 1 or len(ans) == 0:
            return -1
        else:
            return ans[0]

# N명의 사람들이 1~N까지 라벨링 되어있다.
# 그중에 한명만이 town judge이다.
# 1. town judge는 아무도 믿지않지만,
# 2. 다른 사람들은 다 town judge를 믿는다
# 3. a->b 에이가 비를 믿는다.
# 이 경우 모든 그래프를 다 돌때까지 b는 다른사람을 믿는게 나오면 안된다.
'''
심플하게 생각했다.
judge가 마을에 한명만 존재할 수 있는 조건
1. 진입차수가 N-1만큼 있어야한다.
2. 진출차수가 0이여야 한다.

-> 그래서 1을 만족하는 사람 중에 진출차수가 0인 사람을 찾은 후,
그 찾은 사람의 수가 1인 경우 그 사람이 judge라서 해당 이름을 출력하고.
1을 초과하거나 0인 경우 -1을 출력한다.
'''