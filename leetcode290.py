class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        match = {}
        reverse = {}
        ss = str.split(' ')
        if len(pattern) != len(ss):
            return False
        for index, c in enumerate(pattern):
            if c not in match:
                if ss[index] not in reverse:
                    match[c] = ss[index]
                    reverse[ss[index]] = c
                else:
                    return False
            if match[c] != ss[index]:
                return False
        return True

if __name__ == '__main__':
    S = Solution()
    print(S.wordPattern(pattern = "aaa", str = "aa aa aa aa"))
