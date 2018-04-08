class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = [0]*len(s)
        for i in range(len(s)):
            set1 = set()
            length[i] = 1
            set1.add(s[i])
            for j in range(i+1,len(s)):
                if s[j] in set1:
                    break
                length[i] += 1
                set1.add(s[j])
        if not len(s):
            return 0
        return max(length)
