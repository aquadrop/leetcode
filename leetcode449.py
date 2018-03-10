# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        strings = []
        def pre_search(node):
            if not node:
                return
            strings.append(node.val)
            pre_search(node.left)
            pre_search(node.right)

        pre_search(root)
        return '#'.join(str(s) for s in strings)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if not data:
            return None

        strings = data.split('#')

        def insert(x, node):
            if x < node.val:
                if not node.left:
                    node.left = TreeNode(x)
                else:
                    insert(x, node.left)
            elif x > node.val:
                if not node.right:
                    node.right = TreeNode(x)
                else:
                    insert(x, node.right)
            else:
                node.right = TreeNode(x)

        t = TreeNode(int(strings[0]))
        for i in range(1, len(strings)):
            insert(int(strings[i]), t)

        return t

if __name__ == '__main__':
    C = Codec()
    t = TreeNode(2)
    t1 = TreeNode(1)
    t2 = TreeNode(3)

    t.left = t1
    t.right = t2

    print(C.deserialize(C.serialize(t)))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))