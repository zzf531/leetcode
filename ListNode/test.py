class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        aa = ListNode(data)
        if self.head is None:
            self.head = aa
            self.tail = aa
        else:
            self.tail.next = aa
            self.tail = aa
        print('新增元素', self.tail.val)

    def iter(self):
        count = 0
        current = self.head
        if not current:
            return
        while current:
            count +=1
            print(current.val, ',', end='')
            current = current.next
        print('')
        print('元素个数为',  count)

    def search(self, item):
        current = self.head
        while current:
            if current.val == item:
                print(True)
                return
            else:
                current = current.next
        print(False)


link_list = LinkedList()
link_list.append(1)
link_list.append(2)
link_list.iter()
link_list.search(1)