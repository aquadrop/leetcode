class Solution(object):
    def searchInsert(self, nums, target):
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
            if target < nums[mid]:
                end = mid - 1
            if target > nums[mid]:
                begin = mid + 1
        return begin

if __name__ == '__main__':
    S = Solution()
    print(S.searchInsert([1,3,5,6], 5))