class Solution:

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return ['']
        if n == 1:
            return ['()']

        pt = self.generateParenthesis(n - 1)

        new_list = set()
        for p in pt:
            for i in range(len(p)):
                if i == 0:
                    new_p = '()' + p
                    new_list.add(new_p)
                elif i > 0 and i <= len(p) - 1:
                    new_p = p[0:i] + '()' + p[i:]
                    new_list.add(new_p)
                else:
                    new_p = p + '()'
                    new_list.add(new_p)

        return list(new_list)

if __name__ == '__main__':
    S = Solution()
    print(S.generateParenthesis(3))





