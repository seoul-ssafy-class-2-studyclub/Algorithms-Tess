# class Solution(object):
#     def minSubArrayLen(self, s, nums):
#         if nums == []: return 0
#         mysum = 0
#         pin = 0
#         N = len(nums)
#         mylength = 1e9
#         templength = 1
#         for idx in range(N):
#             mysum += nums[idx]
#             templength += 1
#             if mysum >= s and mylength > templength:
#                 print(templength)
#                 mylength = templength
#
#             while mysum >= s:
#                 mysum -= nums[pin]
#                 pin += 1
#                 print(mysum, templength)
#                 if mysum >= s and mylength > templength:
#                     mylength = templength
#                 templength -= 1
#                 if mysum <= s:
#                     if mylength > templength:
#                         mylength = templength
#         if mylength == 1e9: return 0
#         return mylength
#
#
# solution = Solution()
# print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))


class Solution(object):
    def minSubArrayLen(self, s, nums):
        if nums == []: return 0
        mysum = 0
        pin = 0
        N = len(nums)
        mylength = 1e9
        templength = 1
        for idx in range(N):
            mysum += nums[idx]
            templength += 1
            while mysum >= s:
                mysum -= nums[pin]
                pin += 1
                templength -= 1
                if mysum <= s:
                    if mylength > templength:
                        mylength = templength
                        if mylength == 1: return 1
        if mylength == 1e9: return 0
        return mylength

solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))