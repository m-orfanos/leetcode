from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_list_node(xs: List) -> Optional[ListNode]:
    h = None
    for x in xs:
        if h is None:
            h = ListNode(x)
            p = h
        else:
            p.next = ListNode(x)
            p = p.next
    return h


def list_node_to_list(h: Optional[ListNode]) -> List:
    l = []
    p = h
    while p is not None:
        l.append(p.val)
        p = p.next
    return l
