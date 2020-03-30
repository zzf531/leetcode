class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            if s[p1] != s[p2]:
                # 舍弃左字符
                a = s[p1 + 1: p2 + 1]
                # 舍弃右字符
                b = s[p1:p2]
                # 判断是否为回文字符串
                return a[::-1] == a or b[::-1] == b
            p1 += 1
            p2 -= 1
        return True


a =Solution()
print(a.validPalindrome("abbbbca"))