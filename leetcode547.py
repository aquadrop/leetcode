class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        count = 0

        circle = {}

        m = len(M)
        n = len(M[0])

        for i in range(m):
            for j in range(n):
                if M[i][j] == 1 and (i, j) not in circle:
                    # up
                    a = i - 1
                    b = j
                    if a >= 0:
                        if M[a][b] == 1:
                            circle[(i, j)] = circle[(a, b)]





if __name__ == '__main__':
    S = Solution()
    a = S.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    print(a)
    a = S.calculateMinimumHP([[0,-3]])
    print(a)
    a = S.calculateMinimumHP([[1,-2,3],[2,-2,-2]])
    print(a)