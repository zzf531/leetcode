class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root):
        def depth(node):
            if not node: return 0
            print('当前node节点:', node.val)
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, R + L + 1)
            print('当前最大深度:', self.ans)
            print('maxL,R:', (L,R) ,max(L, R) + 1)
            print('____________')
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


T1 = TreeNode(1)
T2 = TreeNode(2)
T3 = TreeNode(3)
T4 = TreeNode(4)
T5 = TreeNode(5)
T6 = TreeNode(6)

T7 = TreeNode(7)
T8 = TreeNode(0)
T9 = TreeNode(8)

T1.left = T2
T2.left = T3
T2.right = T4
T4.right = T5
T5.right = T6

T1.right = T7

a = Solution()
print(a.diameterOfBinaryTree(T1))
