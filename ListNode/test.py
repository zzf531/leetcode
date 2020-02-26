


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 定义一个进位标志
        a, b, p, carry = l1, l2, None, 0
        while a or b:
            # a和b节点的值相加，如果有进位还要加上进位的值
            val = (a.val if a else 0) + (b.val if b else 0) + carry
            # 根据val判断是否有进位,不管有没有进位，val都应该小于10
            carry, val = val / 10 if val >= 10 else 0, val % 10
            p, p.val = a if a else b, val
            # a和b指针都前进一位
            a, b = a.next if a else None, b.next if b else None
            # 根据a和b是否为空，p指针也前进一位
            p.next = a if a else b
        # 不要忘记最后的边界条件，如果循环结束carry>0说明有进位需要处理这个条件
        if carry:
            p.next = ListNode(carry)
        # 每次迭代实际上都是将val赋给a指针的，所以最后返回的是l1
        return l1