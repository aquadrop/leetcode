class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_reach = 0

        for i, n in enumerate(nums):
            if i + n > max_reach and i <= max_reach:
                max_reach = i + n

        return max_reach >= len(nums) - 1

if __name__ == '__main__':
    S = Solution()
    print(S.canJump([3,2,1,0,4]))
