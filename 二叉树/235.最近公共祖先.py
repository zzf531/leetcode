class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            print('第一个条件', p.val, q.val)
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root.val

    def iteration(self, root, p, q):
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node

    def c(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root

T1 = TreeNode(6)
T2 = TreeNode(2)
T3 = TreeNode(0)
T4 = TreeNode(4)
T5 = TreeNode(3)
T6 = TreeNode(5)

T7 = TreeNode(8)
T8 = TreeNode(7)
T9 = TreeNode(9)

T1.left = T2
T2.left = T3
T3.right = T4
T4.left = T5
T4.right = T6

T1.right = T7
T7.left = T8
T7.right = T9

a = Solution()
print(a.lowestCommonAncestor(T1,T3,T6))
