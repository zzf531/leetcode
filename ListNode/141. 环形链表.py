class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        if(head == None or head.next == None):
            return False
        node1 = head
        node2 = head
        while node1 != node2:
            if node2 == None or node2.next == None:
                return False
            node1 = node1.next
            node2 = node2.next.next

        return True


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2


a = Solution()
print(a.hasCycle(l1))

# a = 10
# while a:
#     print(l1.val)
#     l1 = l1.next
#     a -= 1