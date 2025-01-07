package com.morfanos.solutions;

import java.util.LinkedList;
import java.util.Queue;

import com.morfanos.shared.TreeNode;

class LT0226_InvertBinaryTree {

    static TreeNode invertTree(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add(root);
        while (!q.isEmpty()) {
            var n = q.poll();
            if (n == null) {
                continue;
            }

            var t = n.left;
            n.left = n.right;
            n.right = t;

            q.add(n.left);
            q.add(n.right);
        }
        return root;
    }

}
