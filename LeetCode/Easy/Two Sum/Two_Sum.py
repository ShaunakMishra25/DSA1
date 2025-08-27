class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map={}
        for i,num in enumerate(nums):
            comp=target-num
            if comp in num_map:
                return [num_map[comp],i]
            num_map[num]=i