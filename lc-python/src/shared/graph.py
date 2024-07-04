from typing import Optional, List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def list_graph_to_graph(l: List[List[int]]) -> Optional[Node]:
    if not l:
        return None

    ans = {}
    for i, neighbors in enumerate(l):
        # leetcode graphs are 1-indexed
        i += 1
        if i not in ans:
            ans[i] = Node(i)

        if not neighbors:
            continue

        curr = ans[i]

        for neighbor in neighbors:
            if neighbor not in ans:
                ans[neighbor] = Node(neighbor)

            is_missing = True
            for cneighbor in curr.neighbors:
                if cneighbor.val == neighbor:
                    is_missing = False
                    break
            if is_missing:
                curr.neighbors.append(ans[neighbor])

    return ans[1]


def graph_to_list_graph(node: Optional[Node]) -> List[int]:
    if not node:
        return []

    graph = {}
    stack = [node]
    while stack:
        n = stack.pop()
        if n.val in graph:
            continue
        graph[n.val] = []
        for neighbor in n.neighbors:
            graph[n.val].append(neighbor.val)
            stack.append(neighbor)

    l = []
    for v in sorted(graph.keys()):
        l.append(graph[v])

    return l
