package com.morfanos;

import static com.morfanos.LT0098ValidateBinarySearchTree.isValidBST;
import static com.morfanos.shared.Helper.toTreeNode;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class LT0098ValidateBinarySearchTreeTest {

    @Test
    void isValidBST1() {
        var t = toTreeNode(Arrays.asList(2, 1, 3));
        var actual = isValidBST(t);
        assertTrue(actual);
    }

    @Test
    void isValidBST2() {
        var t = toTreeNode(Arrays.asList(5, 1, 4, null, null, 3, 6));
        var actual = isValidBST(t);
        assertFalse(actual);
    }

}
