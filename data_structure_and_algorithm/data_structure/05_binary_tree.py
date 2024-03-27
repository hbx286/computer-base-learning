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
        """层序遍历"""
        pass


    def preorder_traversal(self):
        """前序遍历, 根左右"""
        pass


    def inorder_traversal(self):
        """中序遍历, 左根右"""
        pass


    def postorder_traversal(self):
        """后序遍历, 左右根"""
        pass



        