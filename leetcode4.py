class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        longtest = 1
        p = 0
        q = 0
        index = {}
        flag = False
        for i, s_ in enumerate(s):
            if s_ not in index:
                index[s_] = i
            else:
                flag = True
                r = index[s_]
                length = i - r
                if length > longtest:
                    longtest = length
                index[s_] = i
        if not flag:
            return len(s)
        return longtest
        

if __name__ == '__main__':
    S = Solution()
    print(S.lengthOfLongestSubstring('au'))
