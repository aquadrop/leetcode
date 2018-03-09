class TreeNode:
    def __init__(self, x, index):
        self.left = None
        self.right = None
        self.index = index
        self.val = x
        self.count = 0

class Solution:

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        count = [0 for _ in range(len(nums))]
        nums.reverse()
        t = TreeNode(nums[0], 0)
        for i in range(1, len(nums)):
            self.insert(nums[i], i, t, count)
        count.reverse()
        return count

    def insert(self, x, index, node, counter):
        if x <= node.val:
            node.count += 1
            if not node.left:
                node.left = TreeNode(x, index)
            else:
                self.insert(x, index, node.left, counter)
        elif x > node.val:
            counter[index] += node.count + 1
            if not node.right:
                node.right = TreeNode(x, index)
            else:
                self.insert(x, index, node.right, counter)

if __name__ == '__main__':
    S = Solution()
    print(S.countSmaller([5, 2, 6, 1]))
