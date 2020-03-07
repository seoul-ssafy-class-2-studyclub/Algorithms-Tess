# O(1)로 정렬해야 하는게 요구조건인데
# in-place sorting(제자리 정렬)을 원함

# sorted 된 array를 받는다.
# 다른 array를 사용하지 않은채 swap만 해서 찾는다.

# [1, 1, 2] -> [1, 2, 2]

# 들어오는 애랑 앞에있는애랑 swap하는데, 앞에있는 애가 다를때만 swap하는거임
# 중복되는 것이 아닌걸 발견하면,
# replace하면된다.


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


ans = 0
head = 0 # 기준점을 잡는다.
for idx in range(1, len(nums)):
    if nums[idx] != nums[head]: # 0 앞에 1이 있다면, nums[head]가 0인상태인데,
        head += 1 # 1
        nums[head] = nums[idx] #  0에 1이 들어간다.
        ans += 1
print(ans+1)
print(nums)


''' 제출코드
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        head = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[head]:
                head += 1
                # nums[head], nums[idx] = nums[idx], nums[head]
                nums[head] = nums[idx]
                ans += 1
        return ans+1
'''