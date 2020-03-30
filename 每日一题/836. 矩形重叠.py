class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def change(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (change(rec1[0], rec1[2], rec2[0], rec2[2]) and
                change(rec1[1], rec1[3], rec2[1], rec2[3]))


a = Solution()
print(a.isRectangleOverlap([0,0,2,2], [1,1,3,3]))