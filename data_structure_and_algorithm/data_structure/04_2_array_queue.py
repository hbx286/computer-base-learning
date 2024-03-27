# 基于数组实现的队列

class ArrayQueue:
    def __init__(self, value, length: int) -> None:
        self.value = value
        self.length = length
        self.queue = [None] * self.length
        # 定义尚不完整 对于数组实现的队列可以再添加队首和队尾指向，但耗费更多的空间，但执行的效率会高

    def capacity(self) -> int:
        """获取队列的容量"""
        pass