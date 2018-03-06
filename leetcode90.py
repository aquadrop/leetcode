class Solution:

    res_set = set()

    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        return self.subsetsWithDup2(nums)

    def subsetsWithDup2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 1:
            return [[nums[0]], []]

        not_choose = self.subsetsWithDup2(nums[1:])
        choose = self.subsetsWithDup2(nums[1:])
        [a.insert(0, nums[0]) for a in choose]

        nc = not_choose + choose
        selected = []
        for m in nc:
            if self.check_set(m):
                self.add_set(m)
                selected.append(m)

        return selected

    def add_set(self, subset):
        self.res_set.add(''.join(str(x) for x in subset))

    def check_set(self, subset):
        return not ''.join(str(x) for x in subset) in self.res_set

if __name__ == '__main__':
    S = Solution()
    print(S.subsetsWithDup([1,2, 2]))