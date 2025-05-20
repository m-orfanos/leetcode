package com.morfanos.solutions;

import com.morfanos.shared.TreeNode;

class LT0108ConvertSortedArrayToBinarySearchTree {

    private static TreeNode go(int[] ns, int lhs, int rhs) {
        if (lhs >= rhs) {
            return null;
        }
        var mid = lhs + (rhs - lhs) / 2;

        var t = new TreeNode(ns[mid]);
        t.left = go(ns, lhs, mid);
        t.right = go(ns, mid + 1, rhs);

        return t;
    }

    static TreeNode sortedArrayToBST(int[] nums) {
        return go(nums, 0, nums.length);
    }

}
