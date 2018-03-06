class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_max_reach = 0
        max_reach = 0
        count = 0
        i = 0

        while i < len(nums):
            if max_reach >= len(nums) - 1:
                return count
            cc = current_max_reach
            k = i
            for j in range(i, cc + 1):
                if j <= current_max_reach and j + nums[j] > current_max_reach:
                    current_max_reach = j + nums[j]
                    k = j
                    if current_max_reach > max_reach:
                        max_reach = current_max_reach
                        # count += 1
            count += 1
            i = k
            i = i + 1
        return count

if __name__ == '__main__':
    S = Solution()
    print(S.jump([2,3,1,1,4]))
