class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])


    slo = "My name is Faizan"
    lengthOfLastWord(slo)

