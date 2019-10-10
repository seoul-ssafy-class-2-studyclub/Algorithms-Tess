# https://wayhome25.github.io/cs/2017/04/03/cs-03/

from functools import reduce

# 문제1. 전통적으로 최대값 구하기
def maximum(li):
    default = 0
    for e in li:
        if default < e:
            default = e
    return default
maximum(li)

# 문제1. reduce 활용하여 최대값 구하기
reduce(lambda a,b: a if a > b else b ,li)