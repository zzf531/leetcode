class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1



T1 = TreeNode(1)
T2 = TreeNode(4)
T3 = TreeNode(20)
T4 = TreeNode(15)
T5 = TreeNode(7)

T1.left = T2
T1.right = T3
T3.left = T4
T3.right = T5

a = Solution()
print(a.maxDepth(T1))
