'''

nlogn으로 하는 방법
길이 N의 수열 A가 주어진다. A의 원소들을 각각 A[1], A[2], ... , A[N]이라고 할 때 i < j 인데 A[i] > A[j] 라면 (A[i], A[j])를 Inversion이라고 한다. (단, 1 ≤ i < j ≤ N)
주어진 순열에서 Inversion의 수를 구하는 프로그램을 작성하라.
merge sort 활용


'''
import sys
sys.stdin = open('3998.txt', 'r')
T = int(input())
# datas = [1,2,4,5,8,2,3,6,7,9]

N = int(input())
counting = [0]*N
# 일단 리스트를 정렬된 애들만 리스트로 만든다.
datas = list(map(int, input().split()))





