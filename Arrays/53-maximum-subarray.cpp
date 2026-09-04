
// LeetCode 53 - Maximum Subarray
//
// Approach:
// Use Kadane's Algorithm. At each element, decide whether to
// extend the current subarray or start a new subarray.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i=1; i<nums.size(); i++ )
        {
            currentSum = max(currentSum + nums[i], nums[i]);
            maxSum = max(currentSum, maxSum);
        }

        return maxSum;
    }
};