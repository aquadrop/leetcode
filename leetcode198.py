class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        m = [0] * len(nums)

        m[0] = nums[0]
        m[1] = m[0] if m[0] > nums[1] else nums[1]

        for i in range(2, len(nums)):
            c = nums[i] + m[i - 2]
            m[i] = c if c > m[i - 1] else m[i - 1]
        return m[len(nums) - 1]


if __name__ == '__main__':
    S = Solution()
    print(S.rob([5,2,6,3,1,7]))