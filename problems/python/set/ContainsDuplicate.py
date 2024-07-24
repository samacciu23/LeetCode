# source: https://leetcode.com/problems/contains-duplicate

'''
DESCRIPTION:
Given an integer array nums, return true 
if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

class MySolution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num in counts:
            if counts[num] > 1:
                return True

        return False
    

class BestSolution(object):
    def containsDuplicate(self, nums):
        hashset = set()     
        for i in nums:
            if i in hashset:
                    return True
            hashset.add(i) 
        return False