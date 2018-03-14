class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        index_stack = []
        if len(s) <= 1:
            return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == '(':
                dp[i] = 0
                stack.append(s[i])
                index_stack.append(i)
                continue

            if len(stack) == 0:
                dp[i] = 0
            else:
                if i - 1 >= 0:
                    if s[i - 1] == ')':
                        dp[i] = 1 + dp[i - 1]
                    else:
                        dp[i] = 1
                stack = stack[0:-1]
                p = index_stack[-1]
                if len(index_stack) > 1:
                    index_stack = index_stack[0:-1]
                else:
                    index_stack = []
                if p - 1 >= 0:
                    dp[i] = dp[i] + dp[p - 1]
                # p += 2
        return max(dp) * 2




if __name__ == '__main__':
    S = Solution()
    a = S.longestValidParentheses(")(((((()())()()))()(()))(")
    print(a)