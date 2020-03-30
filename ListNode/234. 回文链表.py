from ListNode.List_node_Base import ListNode, generateList, printList


def isPalindrome(head):
    vals = []
    current_node = head
    while current_node:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]


l1 = generateList([1, 2, 3, 3, 2, 1])
print(isPalindrome(l1))
