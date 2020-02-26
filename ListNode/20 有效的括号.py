class Solution(object):
    def isValid(self, s):
        print(s)
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''




a = Solution()
print(a.isValid('({)}'))
