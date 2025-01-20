package com.morfanos;

import com.morfanos.shared.TreeNode;

class LT0098ValidateBinarySearchTree {

    private static boolean dfs(TreeNode n, long min, long max) {
        if (n == null) {
            return true;
        }
        return min < n.val && n.val < max
                && dfs(n.left, min, n.val)
                && dfs(n.right, n.val, max);
    }

    static boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

}
