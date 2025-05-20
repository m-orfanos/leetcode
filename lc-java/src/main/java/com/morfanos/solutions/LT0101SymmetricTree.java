package com.morfanos.solutions;

import com.morfanos.shared.TreeNode;

class LT0101SymmetricTree {

    private static boolean go(TreeNode m, TreeNode n) {
        if (m == null && n == null) {
            return true;
        }
        if (m == null || n == null || m.val != n.val) {
            return false;
        }
        return go(m.left, n.right) && go(m.right, n.left);

    }

    static boolean isSymmetric(TreeNode root) {
        return go(root.left, root.right);
    }

}
