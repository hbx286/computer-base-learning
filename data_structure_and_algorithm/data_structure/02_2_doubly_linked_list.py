class DoublyLinkedListNode:
    """双向链表结点"""

    def __init__(self, value) -> None:
        self.value = value
        self.next: DoublyLinkedListNode | None = None
        self.preview: DoublyLinkedListNode | None = None


class DoublyLinkedList:
    """双向链表"""

    def __init__(self, node: DoublyLinkedListNode | None = None) -> None:
        self.head = node
        self.tail = node


    def header_insert(self, value) -> None:
        """头插法"""
        new_node = DoublyLinkedListNode(value)
        if self.head:
            new_node.next = self.head
            self.head.preview = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node


    def tail_insert(self, value) -> None:
        """尾插法"""
        new_node = DoublyLinkedListNode(value)
        if self.tail:
            self.tail.next = new_node
            new_node.preview = self.tail
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node


    def insert_into_index(self, value, index: int) -> bool:
        """插入链表的第 index 个结点前, 即插入的值在第 index 个位置"""
        assert index >= 1, IndexError
        head = self.head
        new_node = DoublyLinkedListNode(value)
        while head and index != 2:
            index -= 1
            head = head.next
        if head:
            new_node.next = head.next
            new_node.preview = head
            if head.next:
                head.next.preview = new_node
            head.next = new_node
            if not new_node.next:
                self.tail = new_node
            return True
        if not head and index == 1:
            self.head = new_node
            self.tail = new_node
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


    def traverse_by_header(self) -> None:
        """从头遍历"""
        head = self.head
        while head:
            print(head.value, end=' ', sep='')
            if head.next:
                print("->", end=' ', sep='')
            head = head.next
        print("")


    def traverse_by_tail(self) -> None:
        """从尾遍历"""
        tail = self.tail
        while tail:
            print(tail.value, end=' ', sep='')
            if tail.preview:
                print("<-", end=' ', sep='')
            tail = tail.preview
        print("")


    def remove(self, index: int) -> None:
        """删除第 index 个结点"""
        assert index >= 1, IndexError
        head = self.head
        # if index == 1 and self.head.next:
        #     self.head = self.head.next
        #     return
        # elif index == 1 and not self.head.next:
        #     self.head = None
        #     self.tail = None
        #     return

        while head and index != 2:
            head = head.next
            index -= 1

        # if index == 2:
        #     head.next = head.next.next
        #     if not head.next:
        #         self.tail = None


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


    def access(self, index: int) -> DoublyLinkedListNode:
        """访问第 index 个结点"""
        head = self.head
        while head:
            if index == 1:
                return head
            index -= 1
            head = head.next
        return None


if __name__ == '__main__':
    h_node1 = DoublyLinkedListNode(1)
    h_node2 = DoublyLinkedListNode(2)
    h_node3 = DoublyLinkedListNode(3)
    h_node4 = DoublyLinkedListNode(4)
    h_node5 = DoublyLinkedListNode(5)

    hdll = DoublyLinkedList(h_node1)
    hdll.header_insert(2)
    hdll.header_insert(3)
    hdll.header_insert(4)
    hdll.header_insert(5)
    # hdll.traverse_by_header()
    hdll.traverse_by_tail()

    hdll.header_insert(6)
    # hdll.traverse_by_header()
    hdll.traverse_by_tail()
    hdll.tail_insert(7)
    # hdll.traverse_by_header()
    hdll.traverse_by_tail()
    hdll.insert_into_index(8, 8)
    hdll.traverse_by_tail()
    hdll.traverse_by_header()
    # hdll.remove(1)
    # hdll.traverse_by_header()
    # hdll.traverse_by_tail()
    