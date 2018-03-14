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
        i = 0
        index = {}
        for i, s_ in enumerate(s):
            if s_ not in index:
                index[s_] = i
            else:
                r = index[s_]
                if r >= p:
                    p = r + 1
                index[s_] = i
            length = i - p + 1
            if length > longtest:
                longtest = length
        # length = i - p + 1
        # if length > longtest:
        #     longtest = length
        return longtest
        

if __name__ == '__main__':
    S = Solution()
    print(S.lengthOfLongestSubstring('au'))
