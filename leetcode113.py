# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        paths = []
        self.search(root, 0, sum, [], paths)
        return paths

    def search(self, node, path_val, sum, path, paths):
        if not node:
            return

        val = node.val
        path_val = path_val + val
        path.append(val)
        if not node.left and not node.right:
            if path_val == sum:
                paths.append(path)

        path_a = []
        path_b = []
        for p in path:
            path_a.append(p)
            path_b.append(p)
        self.search(node.left, path_val, sum, path_a, paths)
        self.search(node.right, path_val, sum, path_b, paths)

if __name__ == '__main__':
    S = Solution()
    a1 = TreeNode(5)
    a2 = TreeNode(4)
    a3 = TreeNode(8)
    a4 = TreeNode(11)
    a5 = TreeNode(13)
    a6 = TreeNode(4)
    a7 = TreeNode(7)
    a8 = TreeNode(2)
    a9 = TreeNode(5)
    a10 = TreeNode(1)

    a1.left = a2
    a1.right = a3
    a2.left = a4
    a3.left = a5
    a3.right = a6
    a4.left = a7
    a4.right = a8
    a6.left  = a9
    a6.right = a10
    print(S.pathSum(a1, 22))