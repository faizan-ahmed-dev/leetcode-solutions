// LeetCode 121 - Best Time to Buy and Sell Stock
//
// Approach:
// Track the lowest stock price seen so far and calculate
// the maximum profit by selling at each later price.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i=0; i<prices.size(); i++)
        {
            if (prices[i] < minPrice)
            {
                minPrice = prices[i];
            }

            else
            maxProfit = max(maxProfit, prices[i] - minPrice);
        }
        return maxProfit;
    }
};