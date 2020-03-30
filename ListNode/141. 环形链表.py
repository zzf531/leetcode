from ListNode.List_node_Base import ListNode, generateList, printList


class Solution(object):
    def hasCycle(self, head):
        if head == None or head.next == None:
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
