from ListNode.List_node_Base import ListNode, generateList, printList


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 定义一个进位标志
        a, b, p, carry = l1, l2, None, 0
        while a or b:
            # a和b节点的值相加，如果有进位还要加上进位的值
            val = (a.val if a else 0) + (b.val if b else 0) + carry
            carry = 1 if val >= 10 else 0  # 根据val值判断,不是0,就是1
            val = val % 10  # 取val十位上的数
            p = a if a else b
            p.val = val
            # a和b指针都前进一位
            a, b = a.next if a else None, b.next if b else None
            p.next = a
            # 根据a和b是否为空，p指针也前进一位
        # 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件
        if carry:
            p.next = ListNode(1)

        # 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1
        return l1


if __name__ == "__main__":
    l1 = generateList([7, 7, 7, 0])
    l2 = generateList([6, 6, 6])
    printList(l1)
    printList(l2)
    s = Solution()
    sum = s.addTwoNumbers(l1,l2)
    printList(sum)
