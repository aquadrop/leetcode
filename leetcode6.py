class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        a = numRows
        b = int(len(s) / (numRows - 1) + 1)
        m = [['' for i in range(b)] for _ in range(numRows)]

        c = 0

        for j in range(b):
            for i in range(a):
                if c >= len(s):
                    break
                if j % 2 == 0:
                    m[i][j] = s[c]
                else:
                    if i % 2 == 0:
                        continue
                    else:
                        m[i][j] = s[c]
                c += 1
        t = ''
        for i in range(a):
            for j in range(b):
                t += m[i][j]
        return t



if __name__ == '__main__':
    S = Solution()
    a = S.convert('PAYPALISHIRING', 3)
    print(a)