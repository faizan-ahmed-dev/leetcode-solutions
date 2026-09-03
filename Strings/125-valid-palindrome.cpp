// LeetCode 125 - Valid Palindrome
//
// Approach:
// Two pointers. Move left and right inward while skipping
// non-alphanumeric characters, then compare characters ignoring case.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;

        while (left < right)
        {
            while (left < right && !isalnum(s[left]))
            {
                left++;
            }
            
            while (left < right && !isalnum(s[right]))
            {
                right--;
            }

            if (tolower(s[left]) != tolower(s[right]))
            {
                return false;
            }
            
            left++;
            right--;
        }

        return true;
    }
    
};