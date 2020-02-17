class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head):
        new_head = None
        while head:
            tmp = head.next  # 备份原来head节点的next地址
            head.next = new_head
            new_head = head
            head = tmp
        return new_head


l1 = ListNode(1)
b = ListNode(2)
c = ListNode(3)
l1.next = b
b.next = c
a = Solution()
k = a.reverseList(l1)
while k:
    print(k.val)
    k = k.next
