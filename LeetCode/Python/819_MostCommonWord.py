import collections
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.": # 이걸로 전처리 하는게 더 효율적이네.
            paragraph = paragraph.replace(c, " ")

        count = collections.Counter(word for word in paragraph.lower().split()) # 이건 처음본다.

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        # 가장 자주 나오는 단어이면서 동시에 banned리스트에 없는 단어
        paragraph = paragraph.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace(';', ' ').replace("'", ' ').split()
        newparagraph = []
        for chr in paragraph:
            if chr not in banned and chr.lower() not in banned:
                newparagraph.append(str(chr.lower()))
        mydict = dict()
        mymax = -1e9
        myans = ''
        for p in newparagraph:
            if mydict.get(p):
                mydict[p] += 1
            else:
                mydict[p] = 1
            if mymax < mydict[p]:
                mymax = mydict[p]
                myans = p
        return myans

# Runtime: 24 ms, faster than 59.77% of Python online submissions for Most Common Word.
# Memory Usage: 11.8 MB, less than 32.14% of Python online submissions for Most Common Word.