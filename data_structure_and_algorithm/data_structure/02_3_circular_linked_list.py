class CircularLinkedListNode:
    """循环链表"""
    
    def __init__(self, value) -> None:
        self.value = value
        self.next: CircularLinkedListNode | None = None
        self.preview: CircularLinkedListNode | None = None