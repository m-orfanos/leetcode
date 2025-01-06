package com.morfanos;

import static com.morfanos.LT0101_SymmetricTree.isSymmetric;
import static com.morfanos.shared.Helper.toTreeNode;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

class LT0101_SymmetricTreeTest {

    @Test
    void isSymmetric1() {
        var a = Arrays.asList(1, 2, 2, 3, 4, 4, 3);
        var t = toTreeNode(a);
        var actual = isSymmetric(t);
        assertTrue(actual);
    }

}
