
def sortColors(nums):
    N = len(nums)
    countingSorting = [0]*3
    for idx in range(N):
        countingSorting[nums[idx]] += 1
    st = 0
    idx = 0
    color = 0
    while st < 3 and countingSorting[st]:
        if countingSorting[st]:
            nums[idx] = color
            countingSorting[st] -= 1
            idx += 1
        if not countingSorting[st]:
            color += 1
            st += 1
    print(nums)

sortColors([2,0,2,1,1,0])


def sortColors(nums):
    p0 = 0
    curr = 0
    N = len(nums)
    p2 = N - 1

    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[curr], nums[p2] = nums[p2], nums[curr]
            p2 -= 1
        else:
            curr += 1
        print(nums)
    print(nums)

sortColors([2,0,1])


