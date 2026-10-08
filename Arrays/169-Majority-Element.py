class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # we can use a dictionary to count how many times a number appears
        # but i will use Boyer-Moore Voting Algorithm

        candidate = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                

            if num == candidate:
                count += 1

            else:
                count -= 1

            
            

        return candidate
            