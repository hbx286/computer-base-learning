from collections import deque
# 二叉树

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinaryTree:

    def __init__(self, node: TreeNode | None) -> None:
        self.root = node


    def level_order_traversal(self):
        """层序遍历, 非递归(利用队列先进先出, 顺序入队)"""
        queue = deque()
        if self.root:
            queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node and node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)
            print(node.value, end=' ', sep=' ')
        print("")
            


    def preorder_traversal(self):
        """前序遍历, 根左右, 非递归(利用栈的先进后出, 右子树先入栈)"""
        stack = deque()
        if self.root:
            stack.append(self.root)
        while stack:
            node = stack.pop()
            print(node.value, end=' ', sep=' ')
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print("")


    def inorder_traversal(self):
        """中序遍历, 左根右, 非递归"""
        pass


    def postorder_traversal(self):
        """后序遍历, 左右根, 非递归"""
        pass


    def level_order_traversal_recursive(self):
        """层序遍历, 递归"""
        pass


    def preorder_traversal_recursive(self):
        """前序遍历, 根左右, 递归"""
        pass 


    def inorder_traversal_recursive(self):
        """中序遍历, 左根右, 递归"""
        pass


    def postorder_traversal_recursive(self):
        """后序遍历, 左右根, 递归"""
        pass





if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    tree = BinaryTree(node1)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    tree.preorder_traversal()
