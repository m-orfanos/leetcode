package com.morfanos;

import com.morfanos.shared.TreeNode;

class LT0110_BalancedBinaryTree {

    static int go(TreeNode n) {
        if (n == null) {
            return 0;
        }

        var lhs = go(n.left);
        var rhs = go(n.right);
        var diff = lhs < rhs ? rhs - lhs : lhs - rhs;

        if (lhs < 0 || rhs < 0 || diff > 1) {
            return -1;
        }

        return 1 + (lhs > rhs ? lhs : rhs);
    }

    static boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        return go(root) != -1;
    }

}
