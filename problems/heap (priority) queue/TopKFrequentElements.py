import heapq
from collections import Counter
import random

class MySolution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqD = {}
        for n in nums:
            freqD[n] = freqD.get(n,0) + 1
        
        freqL = [(-f,n) for n,f in freqD.items()]

        return self.heapq_solution(freqL, k)
        

    def heapq_solution(self, freq_list, k):
        heapq.heapify(freq_list)
        return [heapq.heappop(freq_list)[1] for i in range(k)]


    def sort_solution(self, freq_list, k):
        # FASTER ALTERNATIVE WITH sort()
        freq_list.sort()
        return [freq_list[i][1] for i in range(k)]


class OtherSolutions:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      # return self.bucketsort(nums, k)
      # return self.quickselect_version(nums, k)
      return self.heap_version(nums, k)


    def heap_version(self, nums, k):
        # count O(n)
        # push counts to heap one by one, 
        # pop if size > k
        # limits at O(n lg (k)) 
        # total: O (n + n lg k)
        counts = Counter(nums) 
        h = []
        for n, cnt in counts.items():
            heapq.heappush(h, (cnt, n))
            if len(h) > k:
                heapq.heappop(h)
        return [n for _, n in h]

    def quickselect_version(self, nums, k):
      counts = Counter(nums)
      unique = list(counts.keys())

      def partition(left, right):
        pivot_index = random.randint(left, right)
        # record for comparing
        pivot_freq = counts[unique[pivot_index]]
        # move pivot to end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        store_index = left
        for i in range(left, right):
          if counts[unique[i]] > pivot_freq:   # the condition is reversed here for top k
            unique[i], unique[store_index] = unique[store_index], unique[i]
            store_index += 1
        # put pivot to pivot place
        unique[store_index], unique[right] = unique[right], unique[store_index]
        return store_index

      def quickselect(left, right):
        if left >= right:
          return 

        pivot_index = partition(left, right)
        if k - 1 == pivot_index:
          return 

        if k - 1 < pivot_index:   # This causes O(n), due to one branch recursion
          quickselect(left, pivot_index - 1) 
        else:
          quickselect(pivot_index + 1, right)

      quickselect(0, len(unique)-1)
      return unique[:k]

    def bucketsort(self, nums, k):
      # take the buckets equal to len
      # put num to their frequency buckets
      # then flatten the bucket, and pick the top k
      bucket = [[] for _ in range(len(nums) + 1)]
      for num, freq in Counter(nums).items():
        bucket[freq].append(num)
      flat_list = [item for sublist in bucket for item in sublist]
      return flat_list[-k:]