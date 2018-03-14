class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <=2:
            return n

        m = [0 for _ in range(n + 1)]
        m[0] = 0
        m[1] = 1
        m[2] = 2

        # m = [0 for _ in range(n + 1)]
        for i in range(3, n + 1):
            m[i] = m[i - 1] + m[i - 2]
        return m[n]


if __name__ == '__main__':
    S = Solution()
    print(S.climbStairs(3))