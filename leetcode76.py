class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if len(s) < 10:
            return []

        d = {}

        chars = ''
        for i in range(10):
            chars = chars + s[i]

        key = self.shift(chars)
        d[key] = 1

        for i in range(11, len(s)):
            key = key >> 2
            key = key | self.mapper[s[i]] << 18
            if key in d:
                d[key] = d[key] + 1
            else:
                d[key] = 1

        list_ = list()
        for k, value in d.items():
            if value > 1:
                list_.append(self.unfold(k))
        return list_


    mapper = {'A': 0, 'C':1, 'G':2, 'T':3}

    rm = ['A', 'C', 'G', 'T']

    def shift(self, chars):
        a = 0
        for i in range(len(chars) - 1, 0, -1):
            a = (a << 2) + self.mapper[chars[i]]
        return a

    def unfold(self, value):
        chars = ''
        for i in range(10):
            c = value & 3
            value = value >> 2
            chars += self.rm[c]
        return chars

if __name__ == '__main__':
    S = Solution()
    a = S.shift('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    print(a)

    print(S.unfold(a))
    print(S.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))