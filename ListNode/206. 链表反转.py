from ListNode.List_node_Base import ListNode, generateList, printList


class Solution:
    def reverseList(self, head):
        new_head = None
        while head:
            tmp = head.next  # 备份原来head节点的next地址
            head.next = new_head
            new_head = head
            head = tmp
        return new_head


l1 = generateList([1, 3, 7])
a = Solution()
k = a.reverseList(l1)
printList(k)
