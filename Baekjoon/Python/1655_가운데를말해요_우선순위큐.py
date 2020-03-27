import sys
# sys.stdin = open('1655.txt', 'r')
import heapq

numbers = int(input())
max_heap = [] # 작은 값 중에 큰 값이 앞에 오도록,
min_heap = [] # 큰 값들을 나열하도록,

ans = []
for _ in range(numbers): # 수빈이가 부르는 수의 개수를 받고,
    num = int(input())
    if len(max_heap) == len(min_heap): # 수들의 길이를 비교하고, 같다면 max_heap에 추가
        heapq.heappush(max_heap, (-num, num))
    else: # 같지 않은 경우, min_heap
        heapq.heappush(min_heap, (num, num))
    if min_heap and max_heap[0][1] > min_heap[0][1]: # 만약 min_heap에 값이 담겨있고, 비교했을때, max_heap의 원소가 더 크다면,
        # 아래와 같이 교체한다.
        temp_max = heapq.heappop(max_heap)[1]
        temp_min = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-temp_min, temp_min))
        heapq.heappush(min_heap, (temp_max, temp_max))
    ans.append(max_heap[0][1])
print('\n'.join(map(str,ans)))