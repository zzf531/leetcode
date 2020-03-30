class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generateList(l):
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next


def printList(l: ListNode):
    while l:
        print(l.val, '->', end='')
        l = l.next
    print('')
