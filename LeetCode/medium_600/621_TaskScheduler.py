import collections
def leastInterval(tasks, n):

    print(tasks, n)
    # Count
    counts = collections.Counter(tasks)
    print(counts)



tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(leastInterval(tasks, n))

