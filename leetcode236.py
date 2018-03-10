# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1 = []
        path2 = []

        self.find_path(root, p, path1)
        self.find_path(root, q, path2)

        i = 0
        j = 0

        ancestor = None
        while 1:
            if i >= len(path1) or j >= len(path2):
                break
            if path1[i] == path2[j]:
                ancestor = path1[i]
            i += 1
            j += 1
        return ancestor

    def find_path(self, node, p, path):
        if not node:
            return False

        path.append(node)
        if node == p:
            return True
        if not node.left and not node.right:
            del path[-1]
            return False

        a = self.find_path(node.left, p, path)
        if a:
            return True
        b = self.find_path(node.right, p, path)
        if b:
            return True

        del path[-1]
        return False




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
    print(S.lowestCommonAncestor(a1, a5, a9).val)