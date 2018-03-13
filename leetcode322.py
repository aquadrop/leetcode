class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        sorted(coins)
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            min_ = amount
            flag = False
            for coin in coins:
                n = self.get_num(dp, i, coin)
                if n != -1:
                    flag = True
                    if n < min_:
                        min_ = n
            if flag:
                dp[i] = min_ + 1
        return dp[amount]

    def get_num(self, dp, amount, coin):
        if amount < coin:
            return -1
        return dp[amount - coin]




if __name__ == '__main__':
    S = Solution()
    print(S.coinChange([1]
, 2))