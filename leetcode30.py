class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m1 = dict()
        for w in words:
            if w not in m1:
                m1[w] = 1
            else:
                m1[w] = m1[w] + 1

        l = len(words[0])
        if len(s) < l * len(words):
            return []

        a = []

        p = 0
        window = l * len(words)
        # 'barfoofoobarthefoobarman'
        while p <= len(s) - window + 1:
            c = s[p: p+window]
            m2 = dict()
            for i in range(0, len(c) - l + 1, l):
                word = c[i: i + l]
                if word not in m2:
                    m2[word] = 1
                else:
                    m2[word] = m2[word] + 1
            flag = True
            for k in m1:
                if k not in m2 or m2[k] != m1[k]:
                    flag = False
            for k in m2:
                if k not in m1 or m2[k] != m1[k]:
                    flag = False
            if flag:
                a.append(p)
                p = p + 1
            else:
                p = p + 1

        return a



if __name__ == '__main__':
    S = Solution()
    a = S.findSubstring("aaaaaaaa",["aa","aa","aa"])
    print(a)