class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.left(nums, target), self.right(nums, target)]

    def left(self, nums, target):
        begin = 0
        end = len(nums) - 1
        bound = -1
        while begin <= end:
            mid = int((begin + end) / 2)
            if target == nums[mid]:
                bound = mid
                if mid == 0 | nums[mid - 1] < target:
                    return mid
                end = mid - 1
            if target < nums[mid]:
                end = mid - 1
            if target > nums[mid]:
                begin = mid + 1
        return bound

    def right(self, nums, target):
        begin = 0
        end = len(nums) - 1
        bound = -1
        while begin <= end:
            mid = int((begin + end) / 2)
            if target == nums[mid]:
                bound = mid
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                begin = mid + 1
            if target < nums[mid]:
                end = mid - 1
            if target > nums[mid]:
                begin = mid + 1
        return bound

if __name__ == '__main__':
    S = Solution()
    print(S.searchRange([5,7,7,8,8,10] ,8))