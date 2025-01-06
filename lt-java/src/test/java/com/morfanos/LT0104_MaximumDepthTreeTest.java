package com.morfanos;

import static com.morfanos.shared.Helper.toTreeNode;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class LT0104_MaximumDepthTreeTest {

    @Test
    void maxDepth1() {
        var l = Arrays.asList(3, 9, 20, null, null, 15, 7);
        var t = toTreeNode(l);
        var actual = LT0104_MaximumDepthTree.maxDepth(t);
        assertEquals(3, actual);
    }

}
