package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0100_SameTree.isSameTree;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class LT0100_SameTreeTest {

    @Test
    void isSameTree1() {
        var t1 = toTreeNode(Arrays.asList(1, 2, 3));
        var t2 = toTreeNode(Arrays.asList(1, 2, 3));
        var actual = isSameTree(t1, t2);
        assertTrue(actual);
    }

    @Test
    void isSameTree2() {
        var t1 = toTreeNode(Arrays.asList(1, 2));
        var t2 = toTreeNode(Arrays.asList(1, null, 2));
        var actual = isSameTree(t1, t2);
        assertFalse(actual);
    }

}
