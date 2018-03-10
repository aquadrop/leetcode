class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        a = dict()

        for _s_ in s:
            if _s_ not in a:
                a[_s_] = 1
            else:
                a[_s_] = a[_s_] + 1

        count = 0
        has_1 = 0
        for key, value in a.items():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                has_1 = 1
        return count + has_1

if __name__ == '__main__':
    S = Solution()
    print(S.longestPalindrome('ccc'))