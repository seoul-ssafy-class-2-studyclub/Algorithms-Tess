#
#
#
# def solution(goods, coupons):
#     print(goods, coupons)
#     goods.sort(reverse=True)
#     coupons.sort(reverse=True)
#     print(goods, coupons)
#     answer = 0
#     goodPrevCost = 0
#     goodPrevNums = 0
#     couponPrevNums = 0
#     while goods != [] or coupons != []:
#         if goodPrevNums == 0 and goods != []:
#             goodCost, goodNums = goods.pop(0)
#             goodCost = float(goodCost)
#             goodPrevNums = goodNums
#         if couponPrevNums == 0 and coupons != []:
#             couponRate, couponNums = coupons.pop(0)
#             couponRate = float(couponRate)
#             couponPrevNums = couponNums
#         flag = True
#         for _ in range(goodNums):
#             if flag == True:
#                 answer += int(goodCost - (goodCost*(couponRate/100)))
#                 goodPrevNums -= 1
#                 couponPrevNums -= 1
#             if goodPrevNums == 0 or couponPrevNums == 0:
#                 flag = False
#                 break
#         flag = True
#         if goods == [] and goodPrevNums == 0:
#             break
#         if goods == [] and goodPrevNums != 0:
#             goodPrevCost = goodCost
#             break
#     if len(goods) != 0:
#         for cost, nums in goods:
#             answer += (cost*nums)
#         return answer
#     if len(goods) == 0:
#         answer += (goodPrevCost*goodPrevNums)
#     return int(answer)
#
#
#
# print('answer', solution([[25400,2], [10000,1], [31600,1]], [[5,3], [23,2], [11,2], [9,5]]))
# print('answer', solution([[3100, 2], [7700,1], [3100,2]], [[33,4]]))



def solution(r, delivery):
    print(r, delivery)
    print(delivery[2*3+1])

    # 3 y 에 1 x
    # 0,0에서 상하좌우 다 도는데
    # 다 돌때 두번 이상 지나간 곳은 더이상 안지나가도 될듯

    # 4차원 배열을 만드나?



print('answer', solution(3, [[1,5], [8,3], [4,2], [2,3], [3,1], [3,2], [4,2], [5,2], [4,1]]))
