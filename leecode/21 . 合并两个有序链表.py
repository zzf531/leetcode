class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

a = Solution()
l1 = ListNode(1)
b = ListNode(2)
c = ListNode(5)
l1.next = b
b.next = c

l2 = ListNode(3)
b = ListNode(4)
c = ListNode(6)
l2.next = b
b.next = c

k = a.mergeTwoLists(l1,l2)
while k:
    print(k.val)
    k = k.next
