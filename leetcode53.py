class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        m = [0] * len(nums)
        m[0] = nums[0]
        for i in range(1, len(nums)):
            if m[i - 1] <= 0:
                m[i] = nums[i]
            else:
                m[i] = nums[i] + m[i - 1]
        return max(m)


if __name__ == '__main__':
    S = Solution()
    print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))