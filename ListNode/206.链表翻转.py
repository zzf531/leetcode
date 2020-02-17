class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        per = None
        cur = head
        while cur:
            tmp = cur.next  # 记录当前节点的下一个节点
            cur.next = per
            per = cur
            cur = tmp
        return per




l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

a = Solution()
k = a.reverseList(l1)

while k:
    print(k.val)
    k = k.next