class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:return False
        s = str(x)
        s2 = s[::-1]
        i = int(s2)
        if i == x and x == 0:
            return True
        else:
            return False

a = Solution()
print(a.isPalindrome(0))

