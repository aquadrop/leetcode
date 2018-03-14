class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        for i in range(len(triangle)):
            dp.append([0 for _ in range(len(triangle[i]))])
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[0])):
                up = dp[i - 1][j]
                corner = dp[i - 1][j - 1] if j > 0 else dp[i - 1][j + 1]
                if up < corner:
                    dp[i][j] = up + triangle[i][j]
                else:
                    dp[i][j] = corner + triangle[i][j]
        return max(dp[len(triangle) - 1])

if __name__ == '__main__':
    S = Solution()
    a = S.minimumTotal([[2],
    [3,4],
   [6,5,7],
  [4,1,8,3]])
    print(a)