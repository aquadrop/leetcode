class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])

        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = max(1, dp[m - 1][i + 1] - dungeon[m - 1][i])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                down = max(1, dp[i + 1][j] - dungeon[i][j])
                right = max(1, dp[i][j+1] - dungeon[i][j])
                if down < right:
                    dp[i][j] = down
                else:
                    dp[i][j] = right
        return dp[0][0]

if __name__ == '__main__':
    S = Solution()
    a = S.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    print(a)
    a = S.calculateMinimumHP([[0,-3]])
    print(a)
    a = S.calculateMinimumHP([[1,-2,3],[2,-2,-2]])
    print(a)