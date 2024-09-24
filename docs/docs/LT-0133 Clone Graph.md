---
tags:
- difficulty/medium
- topics/hash-table
- topics/depth-first-search
- topics/breadth-first-search
- topics/graph
---

# 0133 Clone Graph

<https://leetcode.com/problems/clone-graph>

## Description

- Problem statement
    - Given a reference of a node in a connected undirected graph.
    - Return a deep copy (clone) of the graph.
- Constraints
    - The number of nodes in the graph is in the range $[0, 100]$.
    - $1 <= Node.val <= 100$
    - $Node.val$ is unique for each node.
    - There are no repeated edges and no self-loops in the graph.
    - The Graph is connected and all nodes can be visited starting from the given node.
- Examples
    - Example 1
        - Input: $adjList = [[2,4],[1,3],[2,4],[1,3]]$
        - Output: $[[2,4],[1,3],[2,4],[1,3]]$
    - Example 2
        - x
    - Example 3
        - x

## Solutions

### Modified DFS

traverse the graph
at every node, at it to a map and update the neighbours
ignore already visited nodes

```python
def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None
        
    if not node.neighbors:
        return Node(node.val)
        
    visited = set()
    copy = {}
    stack = [node]
    while stack:
        n = stack.pop()
        
        if n.val in visited:
            continue
        visited.add(n.val)
        
        if n.val not in copy:
            copy[n.val] = Node(n.val)
            
        for neighbor in n.neighbors:
            stack.append(neighbor)
            if neighbor.val not in copy:
                copy[neighbor.val] = Node(neighbor.val)
            copy[n.val].neighbors.append(copy[neighbor.val])
            
    return copy[node.val]
```

Time complexity: $O(n)$
Space complexity: $O(n)$
