# 基于链表实现的队列

class QueueNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next: QueueNode | None = None


class LinkedListQueue:
    def __init__(self, node: QueueNode | None) -> None:
        self.head = node
        self.rear = node


    def pop(self):
        """出队"""
        pass


    def push(self):
        """入队"""
        pass


    def peek(self):
        """访问队列元素"""
        pass


    def traverse(self):
        """遍历队列"""
        pass


    def is_empty(self) -> bool:
        """队列是否为空"""
        pass


    def length(self) -> int:
        """队列长度"""
        pass
