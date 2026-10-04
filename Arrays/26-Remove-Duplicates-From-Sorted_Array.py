class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0


        uniqueIndex = 1

        for i in range (1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[uniqueIndex] = nums[i]
                uniqueIndex += 1

        return uniqueIndex