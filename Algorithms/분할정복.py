'''
분할정복이란?
분할 -> 정복 -> 합치기 순으로 상위 데이터를 작게 나눠서 문제를 해결하는 방식
분할: 원래 문제를 분할하여 비슷한 유형의 더 작은 하위 문제들로 나누기
정복: 하위 문제 각각을 재귀적으로 해결, 하위 문제의 규모가 충분히 작으면 문제를 탈출 조건으로 놓고 해결
합치기: 하위 문제들의 답을 합쳐서 원래 문제 해결
'''



# 1. 병합 정렬
def mysum(arr):
    total = 0
    for x in arr: # 큰 리스트에서 원소를 하나씩 꺼내서
        total += x # total에 추가해서
    return total # 모든 원소 순회가 끝나면, total을 리턴한다.
print(mysum([1,2,3,4]))




# 2. 퀵 정렬
'''
반드시 필요한 배열
- 기준 원소보다 작은 숫자들로 이루어진 하위배열
- 기준 원소
- 기준 원소보다 큰 숫자들로 이루어진 하위배열
'''

def qsort(arr):
    if len(arr) < 2: # 원소개수가 0이나 1이면 이미 정렬이 된 상태이므로 가지치기한다.
        return arr

    else:
        pivot = arr[0] # pivot은 아무 값이나 가능하므로 가장 처음에 있는 인덱스를 기준점을 삼는다.
        # less 와 more 둘다 기준점을 제외한 모든 리스트에있는 원소들을 순회하면서,
        # pivot 이하인경우 less에 추가하고, 이상인경우 more에 추가하는데,
        # 이를 재귀적으로 호출한다.
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return qsort(less) + [pivot] + qsort(more)

print(qsort([10, 30, 4, 2, 4, 20, 9]))

