class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        richest = 0

        for customer in accounts:

            wealth = 0

            for money in customer:
                wealth += money

            if wealth > richest:
                richest = wealth

        return richest

