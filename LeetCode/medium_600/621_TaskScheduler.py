

import collections
def leastInterval(tasks, n):
    # Count
    counts = collections.Counter(tasks)
    sortedList = []
    for key, val in counts.items():
        sortedList.append([val, key])
    sortedList.sort(reverse=True)
    print(sortedList) 
    ans = []
    cnt, key = sortedList.pop(0)
    for _ in range(cnt):
        cnt -= 1
        ans.append(key)
        for _ in range(n):
            ans.append(False)
    while sortedList:
        cnt, key = sortedList.pop(0)
        for i in range(len(ans)):
            if ans[i] == False:
                print(ans[i])
                cnt -= 1
                ans[i] = key
                
            else:
                continue
    print(ans)


tasks = ["A", "A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))

