package com.morfanos;

import static com.morfanos.LT0572_SubtreeAnotherTree.isSubtree1;
import static com.morfanos.LT0572_SubtreeAnotherTree.isSubtree2;
import static com.morfanos.LT0572_SubtreeAnotherTree.isSubtree3;
import static com.morfanos.shared.Helper.toTreeNode;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class LT0572_SubtreeAnotherTreeTest {

    // **** Approach 1 **** //
    @Test
    void isSubtree11() {
        var r = toTreeNode(Arrays.asList(3, 4, 5, 1, 2));
        var s = toTreeNode(Arrays.asList(4, 1, 2));
        var actual = isSubtree1(r, s);
        assertTrue(actual);
    }

    @Test
    void isSubtree12() {
        var r = toTreeNode(Arrays.asList(
                4, -9, 5, null, -1, null, 8, -6,
                0, 7, null, null, -2, null, null, null,
                null, -3));
        var s = toTreeNode(Arrays.asList(5));
        var actual = isSubtree1(r, s);
        assertFalse(actual);
    }

    // **** Approach 2 **** //
    @Test
    void isSubtree21() {
        var r = toTreeNode(Arrays.asList(3, 4, 5, 1, 2));
        var s = toTreeNode(Arrays.asList(4, 1, 2));
        var actual = isSubtree2(r, s);
        assertTrue(actual);
    }

    @Test
    void isSubtree22() {
        var r = toTreeNode(Arrays.asList(
                4, -9, 5, null, -1, null, 8, -6,
                0, 7, null, null, -2, null, null, null,
                null, -3));
        var s = toTreeNode(Arrays.asList(5));
        var actual = isSubtree2(r, s);
        assertFalse(actual);
    }

    // **** Approach 3 **** //
    @Test
    void isSubtree31() {
        var r = toTreeNode(Arrays.asList(3, 4, 5, 1, 2));
        var s = toTreeNode(Arrays.asList(4, 1, 2));
        var actual = isSubtree3(r, s);
        assertTrue(actual);
    }

    @Test
    void isSubtree32() {
        var r = toTreeNode(Arrays.asList(
                4, -9, 5, null, -1, null, 8, -6,
                0, 7, null, null, -2, null, null, null,
                null, -3));
        var s = toTreeNode(Arrays.asList(5));
        var actual = isSubtree3(r, s);
        assertFalse(actual);
    }

}
