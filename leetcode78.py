class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [[nums[0]], []]

        not_choose = self.subsets(nums[1:])
        choose = self.subsets(nums[1:])
        [a.insert(0, nums[0]) for a in choose]

        return not_choose + choose

if __name__ == '__main__':
    S = Solution()
    print(S.subsets([1,2,3]))