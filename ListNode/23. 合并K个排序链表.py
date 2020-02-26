class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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


def generateList(l):
    pernode = ListNode(0)
    lastnode = pernode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return pernode.next


def printList(l):
    while l:
        print("%d, " % l.val, end='')
        l = l.next
    print('')


if __name__ == '__main__':
    l1 = generateList([1, 4, 5])
    l2 = generateList([1, 3, 4])
    l3 = generateList([2, 6])
    m = Solution()
    merage = m.mergeKLists([l1,l2,l3])
    printList(merage)
