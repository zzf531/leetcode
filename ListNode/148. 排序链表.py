from ListNode.List_node_Base import ListNode, generateList, printList


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


l1 = generateList([5, 1, 2, 5, 15, 34])
a = Solution()
k = a.sortList(l1)
printList(k)
