class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2(object):  # 暴力
    def getIntersectionNode(self, headA, headB):
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha.val

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
d1 = ListNode('a')
d2 = ListNode('b')

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

d1.next = d2
d2.next = l4

# a = Solution()
# print(a.getIntersectionNode(l1, d1))

while l1:
    print(id(l1))
    l1 = l1.next

while d1:
    print(id(l1))
    d1 = d1.next