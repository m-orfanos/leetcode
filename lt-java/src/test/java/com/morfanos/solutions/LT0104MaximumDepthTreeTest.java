package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0104MaximumDepthTree.maxDepth;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0104MaximumDepthTreeTest {

    @Test
    void maxDepth1() {
        var l = Arrays.asList(3, 9, 20, null, null, 15, 7);
        var t = toTreeNode(l);
        var actual = maxDepth(t);
        assertEquals(3, actual);
    }

}
