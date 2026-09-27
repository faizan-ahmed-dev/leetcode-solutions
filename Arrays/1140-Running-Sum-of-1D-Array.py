class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        sum = 0

        answer = []

        for i in nums:
            sum = sum + i
            answer.append(sum)

        return answer