package com.morfanos.shared;

import java.util.ArrayList;
import java.util.List;

public class Node {

    public int val;
    public List<Node> neighbors;

    public Node() {
        this(0, new ArrayList<Node>());
    }

    public Node(int val) {
        this(val, new ArrayList<Node>());
    }

    public Node(int val, ArrayList<Node> neighbors) {
        this.val = val;
        this.neighbors = neighbors;
    }

}
