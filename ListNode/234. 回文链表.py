class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    vals = []
    current_node = head
    while current_node:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]





l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(3)
l5 = ListNode(2)
l6 = ListNode(1)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

print(isPalindrome(l1))