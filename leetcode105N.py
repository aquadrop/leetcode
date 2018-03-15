# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        t = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == t.val:
                break
        left_vals = inorder[0:i]
        right_vals = inorder[i + 1, :]

        left = self.buildTree(preorder[1:], left_vals)
        right = self.buildTree()

if __name__ == '__main__':
    S = Solution()
    print(S.lengthOfLongestSubstring('au'))
