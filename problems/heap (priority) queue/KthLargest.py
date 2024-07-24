# source: https://leetcode.com/problems/kth-largest-element-in-a-stream/
import heapq

'''
DESCRIPTION:
Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
'''

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
