class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        p = len(nums) -1
        selected = []

        pivot = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            pivot = i

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while k >= pivot and j < k:
                c = nums[i] + nums[j] + nums[k]
                if c == 0:
                    selected.append([nums[i], nums[j], nums[k]])
                    while k > 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                        j += 1
                if c > 0:
                    while nums[k] == nums[k - 1]:
                        k -= 1
                if c < 0:
                    j = j + 1

        return selected


if __name__ == '__main__':
    S = Solution()
    a = S.threeSum([1,1,-2])
    print(a)