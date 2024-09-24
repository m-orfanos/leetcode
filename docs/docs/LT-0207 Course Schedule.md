---
tags:
- difficulty/medium
- topics/depth-first-search
- topics/breadth-first-search
- topics/graph
- topics/topological-sort
---

# 0207 Course Schedule

<https://leetcode.com/problems/course-schedule>

## Description

- Problem statement
    - There are a total of `numCourses` courses you have to take, labelled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.
    - For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
    - Return `true` if you can finish all courses. Otherwise, return `false`.
- Constraints
    - $1 <= numCourses <= 2000$
    - $0 <= prerequisites.length <= 5000$
    - $prerequisites[i].length == 2$
    - $0 <= ai, bi < numCourses$
    - All the pairs $prerequisites[i]$ are unique.
- Examples
    - Example 1
        - Input: $numCourses = 2$, $prerequisites = [ [1,0] ]$
        - Output: $true$
    - Example 2
        - Input: $numCourses = 2$, $prerequisites = [[1,0],[0,1]]$
        - Output: $false$

## Solutions

This problem is basically a "low to detect a cycle in a graph" problem.

### Iterative traversal until a cycle is found

```python
def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # build "from->to" adjacency list
    adjacents = [[] for _ in range(numCourses)]
    for [course, prerequisite] in prerequisites:
        adjacents[prerequisite].append(course)
    
    TODO = 0
    DOING = -1
    DONE = 1
    state = [TODO] * numCourses
    
    for i in range(numCourses):
        s = [i]
        while s:
            n = s[-1]
            if state[n] == DONE:
                s.pop()
                continue
            state[n] = DOING
            
            # add prereqs if not completed
            cnt = len(s)
            for adj in adjacents[n]:
                if state[adj] == DOING:
                    return False
                if state[adj] == TODO:
                    s.append(adj)
                
            # pop stack only if all prereqs completed
            if len(s) - cnt == 0:
                s.pop()
                state[n] = DONE
                
    return True
```

Time complexity: $O(m+n)$
Space complexity: $O(m+n)$
where
m = nb of courses/nodes/vertices
n = nb of prerequisites/links/edges

### Perform a topological sort #review

This is the "correct" solution if you know it exists.

> A topological ordering is possible if and only if the graph has no directed cycles, that is, if it is a directed acyclic graph (DAG)
> <https://en.wikipedia.org/wiki/Topological_sorting>
