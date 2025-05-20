package com.morfanos.solutions;

import java.util.HashMap;
import java.util.Stack;

import com.morfanos.shared.Node;

class LT0133CloneGraph {

    static Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }

        var m = new HashMap<Integer, Node>();
        m.put(node.val, new Node(node.val));

        var s = new Stack<Node>();
        s.add(node);
        while (!s.empty()) {
            var n = s.pop();
            for (var neighbor : n.neighbors) {
                if (!m.containsKey(neighbor.val)) {
                    s.add(neighbor);
                    m.put(neighbor.val, new Node(neighbor.val));
                }
                m.get(n.val).neighbors.add(m.get(neighbor.val));
            }
        }

        return m.get(1);
    }

}
