class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 树遍历堆栈
        stack = [root]
        # 父指针字典
        parent = {root: None}
        # 迭代直到我们找到节点p和q
        while p not in parent or q not in parent:
            node = stack.pop()
            # 遍历树时，继续保存父指针。
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        # 节点p的祖先集（）。
        ancestors = set()
        # 使用父指针处理节点p的所有祖先。
        while p:
            ancestors.add(p)
            p = parent[p]
        # q的第一个祖先出现在
        # p的祖先集()是它们最低的共同祖先。.
        while q not in ancestors:
            q = parent[q]
        return q.val


T1 = TreeNode(3)
T2 = TreeNode(5)
T3 = TreeNode(6)
T4 = TreeNode(2)
T5 = TreeNode(7)
T6 = TreeNode(4)

T7 = TreeNode(1)
T8 = TreeNode(0)
T9 = TreeNode(8)

T1.left = T2
T2.left = T3
T2.right = T4
T4.left = T5
T4.right = T6

T1.right = T7
T7.left = T8
T7.right = T9

a = Solution()
print(a.lowestCommonAncestor(T1, T2, T6))

