# coding: utf-8
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for id, i in enumerate(nums):
            o = target - i
            try:
                idx = nums.index(o)
                if id != idx:
                    return sorted([id, idx])
            except:
                pass