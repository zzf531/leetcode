# encoding: utf-8
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))
        print(self.stack)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


a = MinStack()
print(a.push(1))
print(a.push(2))
print(a.push(3))
print(a.top())
