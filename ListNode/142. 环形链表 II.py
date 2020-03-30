class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        visited = set()

        node = head
        while node:
            if node in visited:
                return node.val
            else:
                visited.add(node)
                node = node.next
        return None


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l2


a = Solution()
print(a.detectCycle(l1))

# a = 10
# while a:
#     print(l1.val)
#     l1 = l1.next
#     a -= 1