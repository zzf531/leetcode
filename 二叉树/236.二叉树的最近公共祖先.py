class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        # 用于存储LCA节点的变量。
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):

        def recurse_tree(current_node):

            # 如果到达分支的末尾，则返回False。
            if not current_node:
                return False

            # 左递归
            left = recurse_tree(current_node.left)
            print('左递归', left)

            # 右递归
            right = recurse_tree(current_node.right)

            # 如果当前节点是p或q中的一个
            mid = current_node == p or current_node == q

            # 如果左、右或中三个标志中的任何两个成为真。
            if mid + left + right >= 2:
                self.ans = current_node

            # 如果三个bool值中的任何一个为True，则返回True。
            return mid or left or right

        # 穿过那棵树
        recurse_tree(root)
        return self.ans.val


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

