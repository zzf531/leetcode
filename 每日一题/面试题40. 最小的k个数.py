import heapq

def getLeastNumbers( nums, k):
    if k == 0: return []

    n, opposite = len(nums), [-1 * x for x in nums[:k]]
    heapq.heapify(opposite)
    for i in range(k, len(nums)):
        if -opposite[0] > nums[i]:
            # 维持堆大小不变
            heapq.heappop(opposite)
            heapq.heappush(opposite, -nums[i])
    return [-x for x in opposite]

print(getLeastNumbers([1,2,3,4,5], 3))


