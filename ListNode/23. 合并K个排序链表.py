from ListNode.List_node_Base import ListNode, generateList, printList

class Solution(object):
    def mergeKLists(self, lists):
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


if __name__ == '__main__':
    l1 = generateList([1, 4, 5])
    l2 = generateList([1, 3, 4])
    l3 = generateList([2, 6])
    m = Solution()
    merage = m.mergeKLists([l1,l2,l3])
    printList(merage)
