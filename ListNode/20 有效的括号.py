class Solution(object):
    def isValid(self, s):
        # The stack to keep track of opening brackets.
        stack = []
        # 用于跟踪映射的哈希映射。这使代码保持非常干净。
        # 也使添加更多类型的括号变得更容易
        mapping = {")": "(", "}": "{", "]": "["}
        # 对于表达式中的每个括号。
        for char in s:
            # 如果字符是右括号
            if char in mapping:
                # 如果不是空的，则从堆栈中弹出最上面的元素
                # 否则，将“”的伪值赋给顶级元素变量
                top_element = stack.pop() if stack else '#'
                print('top_element的值', top_element)
                print(stack)
                # hash中的左括号与顶部的映射
                # 堆栈的元素不匹配，返回false
                if mapping[char] != top_element:
                    return False
            else:
                # 我们有一个开口支架，只要把它推到堆栈上就行了。
                stack.append(char)
        # 最后，如果堆栈是空的，那么我们有一个有效的表达式。
        # 对于（（（）
        return not stack




a = Solution()
print(a.isValid('({})'))
