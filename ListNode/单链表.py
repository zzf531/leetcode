class Node(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


head = None

# 创建一个单链表结构
for count in range(1, 6):
    head = Node(count, head)

# 输出节点内容，输出完后，单链表结构也销毁了
while head != None:
    print(head.val)  # 输出：5, 4, 3, 2, 1
    head = head.next
