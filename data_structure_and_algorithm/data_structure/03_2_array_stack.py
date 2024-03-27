# 基于数组实现的栈

class ArrayStack:

    def __init__(self, value, length: int,) -> None:
        self.length = length
        self.stack = [None] * self.length
        self.stack[0] = value


    def is_empty(self) -> bool:
        """判断栈是否为空"""
        pass


    def push(self, value):
        """入栈"""
        pass


    def pop(self):
        """出栈"""
        pass


    def peek(self):
        """访问栈顶元素"""
        pass


    def length(self):
        """统计长度"""
        pass


    def traverse(self):
        """遍历栈"""
        pass

