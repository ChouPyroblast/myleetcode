"""
one pass hash:
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            if (target - nums[i]) in dic and dic[target - nums[i]] != i :
                return (dic[target - nums[i]], i)
            dic[nums[i]] = i #note that this line must come after the for loop in case there are two indentical values
