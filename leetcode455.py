class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g = sorted(g)
        s = sorted(s)

        num = 0

        i = 0
        j = 0
        while 1:

            if i >= len(g) or j >= len(s):
                return num
            _g = g[i]
            _s = s[j]

            if _s >= _g:
                i += 1
                j += 1
                num += 1
            else:
                j += 1

if __name__ == '__main__':
    S = Solution()
    print(S.findContentChildren([1,2], [1,2,3]))
