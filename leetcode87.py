class TreeNode:
    def __init__(self, val):
        self.val = val
        lens = len(val)
        mid = int(lens / 2)
        if len(val) == 1:
            self.left = None
            self.right = None
        else:
            self.left = TreeNode(val[0: mid])
            self.right = TreeNode(val[mid:])

class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        t = TreeNode(s1)
        sc = self.scramble(t)
        for _s in sc:
            if _s == s2:
                return True
        return False

    def scramble(self, t):
        '''

        :param t: TreeNode
        :return:
        '''
        if len(t.val) == 1:
            return [t.val]
        l = self.scramble(t.left)
        r = self.scramble(t.right)

        sc = []
        for _l in l:
            for _r in r:
                sc.append(_l + _r)
                sc.append(_r + _l)
        return sc




if __name__ == '__main__':
    S = Solution()
    a = S.isScramble('abb', 'bab')
    print(a)
