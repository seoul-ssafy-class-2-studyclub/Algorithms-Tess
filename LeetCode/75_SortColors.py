
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
    N = len(nums)


sortColors([2,0,2,1,1,0])
