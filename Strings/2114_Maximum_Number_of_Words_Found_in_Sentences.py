class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        
        maximum = 0

        for sentence in sentences:
            words = sentence.count(" ") + 1

            if words >  maximum:
                maximum = words

        return maximum