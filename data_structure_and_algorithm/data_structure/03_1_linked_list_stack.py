# 基于链表实现的栈

class StackNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next: StackNode | None = None

class LinkedListStack:

    def __init__(self, node: StackNode | None) -> None:
        self.top = node


    def is_empty(self) -> bool:
        """判断栈是否为空"""
        return self.top is None


    def push(self, value) -> None:
        """入栈"""
        node = StackNode(value)
        node.next = self.top
        self.top = node


    def pop(self) -> None:
        """出栈"""
        if not self.top:
            return None
        self.top = self.top.next if self.top.next else None


    def peek(self):
        """访问栈顶元素"""
        if self.is_empty():
            return None
        print(f"栈顶元素为: {self.top.value}")
        return self.top.value


    def length(self):
        """统计长度"""
        top = self.top
        count = 0
        while top:
            count += 1
            top = self.top.next
        print(f"栈长度为: {count}")
        return count


    def traverse(self):
        """遍历栈"""
        top = self.top
        while top:
            print(top.value, end=' ', sep='')
            top = top.next
            if top:
                print("<-", end=' ',sep='')
        print("")


if __name__ == '__main__':
    stack = LinkedListStack(None)
    print(stack.is_empty(), stack.length())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.peek()
    for i in range(4):
        stack.pop()
        stack.traverse()
    

