class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
b = ListNode(2)
c = ListNode(5)
d = ListNode(7)
l1.next = b
b.next = c
c.next= d
print(b.next.val)
while b:
     print(b.val)
     b = b.next
