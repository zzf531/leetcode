"""链表中的基本要素：

结点(也可以叫节点或元素)，每一个结点有两个域，左边部份叫值域，用于存放用户数据；右边叫指针域，一般是存储着到下一个元素的指针
head结点，head是一个特殊的结节，head结点永远指向第一个结点
tail结点，tail结点也是一个特殊的结点，tail结点永远指向最后一个节点
None，链表中最后一个结点指针域的指针指向None值，因也叫接地点，所以有些资料上用电气上的接地符号代表None
链表的常用方法：

LinkedList() 创建空链表，不需要参数，返回值是空链表
is_empty() 测试链表是否为空，不需要参数，返回值是布尔值
append(data) 在尾部增加一个元素作为列表最后一个。参数是要追加的元素，无返回值
iter() 遍历链表，无参数，无返回值，此方法一般是一个生成器
insert(idx,value) 插入一个元素，参数为插入元素的索引和值
remove(idx)移除1个元素，参数为要移除的元素或索引，并修改链表
size() 返回链表的元素数，不需要参数，返回值是个整数
search(item) 查找链表某元素，参数为要查找的元素或索引，返回是布尔值
 
python用类来实现链表的数据结构，节点（Node）是实现链表的基本模块，每个节点至少包括两个重要部分。
首先，包括节点自身的数据，称为“数据域”(也叫值域)。其次，每个节点包括下一个节点的“引用”(也叫指针)
下边的代码用于实现一个Node类："""


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

    def iter(self):  # 遍历链表, 求链表长度
        count = 0
        current = self.head
        if not current:
            return
        while current:
            count += 1
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