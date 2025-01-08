package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static com.morfanos.shared.Helper.toTreeNode;
import static com.morfanos.solutions.LT0101SymmetricTree.isSymmetric;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0101SymmetricTreeTest {

    @Test
    void isSymmetric1() {
        var a = Arrays.asList(1, 2, 2, 3, 4, 4, 3);
        var t = toTreeNode(a);
        var actual = isSymmetric(t);
        assertTrue(actual);
    }

}
