class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            longest = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > longest:
                        longest = dp[j] + 1
            dp[i] = longest
        return max(dp)


if __name__ == '__main__':
    S = Solution()
    a = S.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    print(a)