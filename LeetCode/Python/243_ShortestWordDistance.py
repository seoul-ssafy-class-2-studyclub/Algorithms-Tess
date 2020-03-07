class Solution(object):
    def shortestDistance(self, words, word1, word2):
        min_dist = len(words)
        curr_word, idx = None, 0
        for i, w in enumerate(words):
            if w not in (word1, word2):
                continue
            if curr_word and w != curr_word: # curr_word에 있고, w가 curr_word가 아닌 경우
                min_dist = min(min_dist, i - idx)
            curr_word, idx = w, i # 가장 처음 발견한 w는 curr_word에 들어간다.
            # 계속 curr_word는 다른 w로 갱신된다.
        return min_dist