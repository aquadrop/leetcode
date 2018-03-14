# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    a = None
    b = None
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        L = []
        self.inorder(root, L)
        for i in range(len(L) - 1):
            if L[i].val > L[i + 1].val:
                temp = L[i].val
                L[i].val = L[i + 1].val
                L[i + 1].val = temp
        return


    def inorder(self, node, L):
        if not node:
            return
        self.inorder(node.left, L)
        L.append(node)
        self.inorder(node.right, L)

if __name__ == '__main__':
    S = Solution()
    print(S.lengthOfLongestSubstring('au'))
