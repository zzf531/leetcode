class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = set(s)
        b = list(a)
        oddc = 0
        flag = 0
        for i in range(len(b)):
            c = s.count(b[i])
            if c % 2 != 0:
                oddc += 1
                flag = 1
        l = len(s) - (oddc - flag)
        return l

a = Solution()
print(a.longestPalindrome('abccccdd'))