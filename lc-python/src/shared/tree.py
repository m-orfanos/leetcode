from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None

    # swap tree nodes
    temp = root.left
    root.left = root.right
    root.right = temp

    # depth-first traversal
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def list_tree_to_tree(l: List[int]) -> Optional[TreeNode]:
    """
    This method converts a binary tree backed up by an array (list) to
    a binary tree modelled by a linked data-structure.
    """

    def insert_tree(val: int, node: Optional[TreeNode]) -> TreeNode:
        if node is None:
            return TreeNode(val)
        if node.val < val:
            node.right = insert_tree(val, node.right)
        elif node.val > val:
            node.left = insert_tree(val, node.left)
        return node

    if len(l) == 0:
        return None
    h = None
    for x in l:
        if x is None:
            continue
        h = insert_tree(x, h)
    return h


def tree_to_list(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    l = [root.val]

    # breadth-first traversal
    q = [root.left, root.right]
    while len(q) > 0:
        n = q.pop(0)
        if n is None:
            continue
        l.append(n.val)
        q.append(n.left)
        q.append(n.right)
    return l
