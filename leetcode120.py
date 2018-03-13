class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp = []
        for i in range(len(triangle)):
            dp.append([0 for _ in range(len(triangle[i]))])

        for i in range(len(triangle[len(triangle) - 1])):
            dp[len(triangle) - 1][i] = triangle[len(triangle)-1][i]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                down = dp[i + 1][j]
                right = dp[i+ 1][j+1]
                if down < right:
                    dp[i][j] = down + triangle[i][j]
                else:
                    dp[i][j] = right + triangle[i][j]

        return dp[0][0]



if __name__ == '__main__':
    S = Solution()
    print(S.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))