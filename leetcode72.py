class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                    continue
                if i == 0:
                    dp[0][j] = j
                    continue
                if j == 0:
                    dp[i][0] = i
                    continue
                a = i - 1
                b = j - 1
                if word1[a] == word2[b]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # replace
                    r = dp[i - 1][j - 1] + 1
                    # insert
                    insert = dp[i][j - 1] + 1
                    # delete
                    delete = dp[i - 1][j] + 1
                    dp[i][j] = min([r, insert, delete])

        return dp[len(word1)][len(word2)]



if __name__ == '__main__':
    S = Solution()
    a = S.minDistance('faig', 'cdfaicx')
    print(a)
