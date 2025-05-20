package com.morfanos.shared;

public class TreeNode {
    public Integer val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode() {
        this(0, null, null);
    }

    public TreeNode(Integer val) {
        this(val, null, null);
    }

    public TreeNode(Integer val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

}
