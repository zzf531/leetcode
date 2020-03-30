class Solution(object):
    def canThreePartsEqualSum(self, A):
        amount = sum(A)
        single = amount / 3
        if single % 1 != 0:
            return False
        s = 0
        l = []
        for i in range(len(A)):
            s += A[i]
            if s == single:
                l.append(s)  # 第一段求出后,加入数组,和清零
                s = 0
                if len(l) == 2 and i != len(A)-1: # 求出前两部分和后,求第三部分     超出索引求和为0,我也不知道
                    c = sum(A[i+1:])
                    l.append(c)
                    return l[1] == l[0] == l[2]
        return False


a = Solution()
print(a.canThreePartsEqualSum([1,-1,1,-1]))
qwe=  [10,-10,10,-10,10,-10,10,-10]