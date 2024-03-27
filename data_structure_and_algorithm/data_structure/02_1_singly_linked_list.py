class SinglyLinkedListNode:
    """单向链表节点"""

    def __init__(self, value) -> None:
        self.value = value
        self.next: SinglyLinkedListNode | None = None


class SinglyLinkedList:
    """单向链表"""

    def __init__(self, head: SinglyLinkedListNode | None = None) -> None:
        self.head = head


    def header_insert(self, value) -> None:
        """头插法"""
        new_node = SinglyLinkedListNode(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node


    def tail_insert(self, value) -> None:
        """尾插法"""
        new_node = SinglyLinkedListNode(value)
        head = self.head
        if head:
            while head and head.next:
                head = head.next
            head.next = new_node
        else:
            self.head = new_node


    def insert_into_index_next(self, value, index: int) -> bool:
        """插入链表的第 index 个结点后, 即插入的值在第 index + 1 个位置"""
        assert index >= 1, IndexError
        new_node = SinglyLinkedListNode(value)
        head = self.head

        if not head:
            self.head = new_node
            return True

        while head and index != 1:
            head = head.next
            index -= 1

        if index == 1:
            new_node.next = head.next if head else None
            head.next = new_node
            return True
        return False


    def insert_into_index_last(self, value, index: int) -> bool:
        """插入链表的第 index 个结点前, 即插入的值在第 index 个位置"""
        assert index >= 1
        new_node = SinglyLinkedListNode(value)
        head = self.head
        if not head and index == 1:
            new_node.next = head
            self.head = new_node
            return True
        
        while head and index != 2:
            head = head.next
            index -= 1
        
        if index == 2:
            new_node.next = head.next if head else None
            head.next = new_node
            return True
        return False


    def length(self):
        count = 0
        head = self.head
        while head:
            count += 1
            head = head.next
        print("链表的长度为", count)
        return count


    def traverse(self) -> None:
        """遍历"""
        head = self.head
        while head:
            print(head.value, end=' ', sep='')
            if head.next:
                print("->", end=' ', sep='')
            head = head.next
        print("")


    def remove(self, index: int) -> None:
        """删除第 index 个结点"""
        assert index >= 1
        head = self.head
        if index == 1 and self.head.next:
            self.head = self.head.next
        elif index == 1 and not self.head.next:
            self.head = None

        while head and index != 2:
            head = head.next
            index -= 1

        if index == 2:
            head.next = head.next.next


    def find(self, value) -> int:
        """查找"""
        head = self.head
        i = 0
        while head:
            if head.value == value:
                return i
            i += 1
            head = head.next
        return -1


    def access(self, index: int) -> SinglyLinkedListNode:
        """访问第 index 个结点"""
        head = self.head
        while head:
            if index == 1:
                return head
            index -= 1
            head = head.next
        return None


if __name__ == '__main__':
    # 头插法
    h_node = SinglyLinkedListNode(1)

    header_sll = SinglyLinkedList(h_node)
    header_sll.header_insert(2)
    header_sll.header_insert(3)
    header_sll.header_insert(4)
    header_sll.traverse()
    print("删除第一个结点: ", end="")
    header_sll.remove(1)
    header_sll.traverse()
    print("删除最后一个结点: ", end="")
    header_sll.remove(3)
    header_sll.traverse()
    print("")

    # 尾插法
    t_node = SinglyLinkedListNode(1)

    tail_sll = SinglyLinkedList(t_node)
    tail_sll.tail_insert(2)
    tail_sll.tail_insert(3)
    tail_sll.tail_insert(4)
    tail_sll.traverse()
    print("删除第一个结点: ", end="")
    tail_sll.remove(1)
    tail_sll.traverse()
    print("删除最后一个结点: ", end="")
    tail_sll.remove(3)
    tail_sll.traverse()
    print("")

    # 普通插入
    sll = SinglyLinkedList(None)
    print("头结点为空: ", end="")
    sll.insert_into_index_next(1, 1)
    sll.traverse()
    print("往第1个位置之后插入: ", end="")
    sll.insert_into_index_next(2, 1)
    sll.traverse()
    print("往第1个位置之前插入: ", end="")
    sll.insert_into_index_last(3, 1)
    sll.traverse()
    print("往第1个位置之后插入: ", end="")
    sll.insert_into_index_next(4, 1)
    sll.traverse()
    print("往第3个位置之前插入: ", end="")
    sll.insert_into_index_last(5, 3)
    sll.traverse()
    print("往第5个位置之后插入: ", end="")
    sll.insert_into_index_next(6, 5)
    sll.traverse()
    sll.length()
    print(f"访问第1个结点: {sll.access(1).value}")
    print(f"访问第5个结点: {sll.access(5).value}")
    print(f"访问第6个结点: {sll.access(6).value}")
