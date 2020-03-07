import collections
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(words1) != len(words2):
            return False
        word_map = collections.defaultdict(set)
        for a, b in pairs:
            word_map[a].add(b)
            word_map[b].add(a)

        for w1, w2 in zip(words1, words2):
            # 둘이 다르고, 없는 경우 비슷하지 않다는 뜻이므로 바로 false
            if w1 != w2 and w2 not in word_map[w1]:
                return False
        return True

'''
# int_dic = defaultdict(int) default값이 int인 딕셔너리
위와 같이 설정을 하면 값을 지정하지 않은 키는 그 값이 0으로 지정된다.
>>> int_dict['key1']
0
>>> int_dict
defaultdict(<class 'int'>, {'key1': 0}) 
default 값으로 set을 줬을때 작동방식 
>>> set_dict = defaultdict(set)
>>> set_dict
defaultdict(<class 'set'>, {})                                     # 디폴트값이 set인 딕셔너리
>>> set_dict['key1']                                              # 값을 지정하지 않으면 빈 리스트로 초기화
set()
>>> set_dict['key2'] = 'test'                                    # 값을 지정하면 해당값으로 초기화
>>> set_dict
defaultdict(<class 'set'>, {'key1': set(), 'key2': 'test'})      



>>> name_list = [('kim','sungsu'), ('kang','hodong'), ('park','jisung'), ('kim','yuna'), ('park','chanho'), ('kang','hodong')]

>>> nset = defaultdict(set)                       # 초깃값을 셋으로 설정

>>> for k, v in name_list:

...     ndict[k].add(v)                                  # list는 append()를 사용해서 항목추가. set은 add()를 사용해서 항목추가

...

>>> ndict
defaultdict(<class 'set'>, {'kim': {'sungsu', 'yuna'}, 'kang': {'hodong'}, 'park': {'jisung', 'chanho'}})
'''