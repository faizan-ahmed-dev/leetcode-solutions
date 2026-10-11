class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        expectedSum = n * (n+1) // 2
        actualSum = sum(nums)

        return expectedSum - actualSum