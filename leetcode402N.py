class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k >= len(num):
            return '0'

        if not num:
            return '0'

        new_str = num[0]
        for i in range(1, len(num)):
            if k == 0:
                break
            b = int(num[i])
            a = int(new_str[-1])
            if b > a:
                k -= 1


        flag = True
        a = ''
        for s in new_str:
            if s == '0' and flag:
                continue
            else:
                flag = False
            a += s

        if not a:
            a = '0'
        return a




if __name__ == '__main__':
    S = Solution()
    print(S.removeKdigits("112",1))