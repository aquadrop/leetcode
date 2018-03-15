class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        if len(s3) != len(s1) + len(s2):
            return False

        if len(s3) == 0 and len(s1) == 0 and len(s2) == 0:
            return True
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[j - 1][0] and s1[j - 1] == s3[j - 1]
        for a in range(1, len(s1) + 1):
            for b in range(1, len(s2) + 1):
                i = a - 1
                j = b - 1
                k = i + j
                if s3[k] != s1[i] and s3[k] != s2[j]:
                    dp[a][b] = False
                if s3[k] == s1[i] and s3[k] != s2[j]:
                    dp[a][b] = dp[a - 1][b]
                if s3[k] != s1[i] and s3[k] == s2[j]:
                    dp[a][b] = dp[a][b - 1]
                if s3[k] == s1[i] and s3[k] == s2[j]:
                    dp[a][b] = dp[a][b - 1] or dp[a - 1][b]

        return dp[len(s1)][len(s2)]




if __name__ == '__main__':
    S = Solution()
    a = S.isInterleave('aabcc', 'dbbca', "aadbbcbcac")
    print(a)
