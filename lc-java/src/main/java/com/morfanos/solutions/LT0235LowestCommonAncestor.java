package com.morfanos.solutions;

import com.morfanos.shared.TreeNode;

import java.util.Stack;

class LT0235LowestCommonAncestor {

    static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p.val > q.val) {
            var t = p;
            p = q;
            q = t;
        }

        Stack<TreeNode> s = new Stack<>();
        s.add(root);
        while (!s.empty()) {
            var n = s.pop();
            if (p.val <= n.val && n.val <= q.val) {
                return n;
            }
            if (n.left != null) {
                s.add(n.left);
            }
            if (n.right != null) {
                s.add(n.right);
            }
        }

        return null;
    }
}
