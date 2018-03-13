class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4:
            return False
        total_length = sum(nums)
        if total_length % 4 != 0:
            return False
        sorted(nums, reverse=True)
        cc = self.combination(nums, len(nums) - 1, total_length)

        for e in cc:
            is_square = True
            for i in range(1, 4):
                if e[i] != e[i - 1]:
                    is_square = False
            if is_square:
                return True
        return False




    def combination(self, nums, n, total_length):
        if n == 3:
            cb = [[[nums[0]], [nums[1]], [nums[2]], [nums[3]]]]
            return cb
        cb = self.combination(nums, n - 1, total_length)
        new = []
        for i in range(len(cb)):
            if self.delete(cb[i], total_length):
                continue
            for j in range(4):
                cb[i][j].append(nums[n])
                new.append(added)
        return new

    def delete(self, combination, total_length):
        for c in combination:
            if sum(c) > total_length / 4:
                return True
        return False


if __name__ == '__main__':
    S = Solution()
    print(S.makesquare([1,1,2,2,2]))