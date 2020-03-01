class Stack:
    # 模拟栈
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 创建一个栈对象，并加入操作方法
s = Stack()
print('栈是否为空', s.isEmpty())
s.push(4)
s.push('DOG')
print('返回栈顶元素', s.peek())
s.push(True)
print('返回栈长度', s.size())
print('栈是否为空', s.isEmpty())
s.push(8.4)
print('删除栈顶元素', s.pop())
print('删除栈顶元素', s.pop())
print('返回栈长度', s.size())
