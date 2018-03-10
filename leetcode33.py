class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                return mid
            if nums[begin] <= nums[mid]:
                if target < nums[mid] and target >= nums[begin]:
                    end = mid - 1
                else:
                    begin = mid + 1
                continue
            if nums[mid] <= nums[end]:
                if target > nums[mid] and target <= nums[end]:
                    begin = mid + 1
                else:
                    end = mid - 1
                continue
        return -1

if __name__ == '__main__':
    S = Solution()
    print(S.search([4,5, 6, 7, 0, 1, 2], 2))