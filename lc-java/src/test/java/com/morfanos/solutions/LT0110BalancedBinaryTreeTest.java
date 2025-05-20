package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0110BalancedBinaryTree.isBalanced;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0110BalancedBinaryTreeTest {

    @Test
    void isBalanced1() {
        var l = Arrays.asList(3, 9, 20, null, null, 15, 7);
        var t = toTreeNode(l);
        var actual = isBalanced(t);
        assertTrue(actual);
    }

    @Test
    void isBalanced2() {
        var l = Arrays.asList(1, 2, 2, 3, 3, null, null, 4, 4);
        var t = toTreeNode(l);
        var actual = isBalanced(t);
        assertFalse(actual);
    }

    @Test
    void isBalanced3() {
        var l = Arrays.asList(1, 2, 2, 3, null, null, 3, 4, null, null, null, null, null, null, 4);
        var t = toTreeNode(l);
        var actual = isBalanced(t);
        assertFalse(actual);
    }

}
