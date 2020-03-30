from ListNode.List_node_Base import ListNode, generateList, printList


class Solution:
    def rotateRight(self, head, k):
        # 基本情况
        if not head:
            return None
        if not head.next:
            return head

        # 将链表关闭到环中
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        print('求n的值', 5)
        old_tail.next = head  # 尾巴和头相连接

        new_tail = head
        print(head.val)
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
            print('新尾巴为:', new_tail.val)
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head


if __name__ == '__main__':
    l = generateList([1, 2, 3, 4, 5])
    # printList(l)
    rotateList = Solution()
    printList(rotateList.rotateRight(l,2))

