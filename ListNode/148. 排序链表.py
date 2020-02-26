class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):  # 放入list排序,放回ListNode
        l = []
        p = head
        while p:
            l.append(p.val)
            p = p.next
        l.sort()
        p = head
        for e in l:
            p.val = e
            p = p.next
        return head


l1 = ListNode(3)
l2 = ListNode(9)
l3 = ListNode(2)
l4 = ListNode(101)
l1.next = l2
l2.next = l3
l3.next = l4

a = Solution()
call_list = a.sortList(l1)
while call_list:
    print(call_list.val)
    call_list = call_list.next