import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

        # create a min-heap
        heapq.heapify(self.nums)

        # violate nums.size > k
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        # violate increasing heap size
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]  # extract the first element
    

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
