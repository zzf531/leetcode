class MinStack:

    # 辅助栈和数据栈不同步
    # 关键 1：辅助栈的元素空的时候，必须放入新进来的数
    # 关键 2：新来的数小于或者等于辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进去）
    # 关键 3：出栈的时候，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈，即"出栈保持同步"就可以了

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        # 关键 1 和关键 2
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        if self.data:
            top = self.data.pop()

            if self.helper and top == self.helper[-1]:
                self.helper.pop()
            return top

    def top(self):
        if self.data:
            return self.data[-1]
    def getMin(self):
        if self.helper:
            return self.helper[-1]



a = MinStack()
print(a.pop())
print(a.push(3))
print(a.push(2))
print(a.push(4))
print(a.pop())
print(a.pop())
print(a.getMin())
