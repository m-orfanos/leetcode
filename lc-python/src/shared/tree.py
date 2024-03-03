from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_tree_to_tree(l: List[int]) -> Optional[TreeNode]:
    """
    This method converts a binary tree backed up by an array (list) to
    a binary tree modeled by a linked data-structure.
    """
    if len(l) == 0:
        return None

    root = TreeNode(l[0])
    q = [root]
    i = 1
    while i < len(l):
        curr = q.pop(0)
        if i < len(l):
            if l[i] is not None:
                curr.left = TreeNode(l[i])
                q.append(curr.left)
            i += 1
        if i < len(l):
            if l[i] is not None:
                curr.right = TreeNode(l[i])
                q.append(curr.right)
            i += 1
    return root


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
