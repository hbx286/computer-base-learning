class Array:
    """数组"""
    array = []

    def __init__(self, length: int, value_type) -> None:
        self.length = length
        self.type_ = value_type
        self.array = [0] * self.length


    def insert(self, value, index: int) -> None:
        """插入"""
        assert type(value) == self.type_, TypeError
        assert index <= self.length, IndexError
        for item in range(index, self.length, -1):
            self.array[item] = self.array[item - 1]
        self.array[index] = value


    def remove(self, index: int) -> None:
        """删除"""
        assert index <= len(self.array) - 1, IndexError
        for item in range(index, len(self.array) - 1):
            self.array[item] = self.array[item + 1]


    def traverse(self) -> None:
        """遍历"""
        for item in range(len(self.array)):
            print(self.array[item], end=' ')
            if item == len(self.array) - 1:
                print('')


    def find(self, value) -> int:
        """查找"""
        assert type(value) == self.type_, TypeError
        for item in range(len(self.array)):
            if self.array[item] == value:
                return item
        return -1



if __name__ == '__main__':
    arr = Array(10, int)
    arr.insert(18, 9)
    arr.insert(10, 5)
    arr.insert(6, 3)
    arr.insert(2, 1)
    arr.traverse()
    print(arr.find(10))
    arr.remove(5)
    arr.traverse()
