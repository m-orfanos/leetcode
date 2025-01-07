package com.morfanos;

import static com.morfanos.LT0108_ConvertSortedArrayToBinarySearchTree.sortedArrayToBST;
import static com.morfanos.shared.Helper.toArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0108_ConvertSortedArrayToBinarySearchTreeTest {

    @Test
    void sortedArrayToBST1() {
        var t = sortedArrayToBST(toArray(-10, -3, 0, 5, 9));
        var actual = toArray(t);
        assertArrayEquals(toArray(0, -3, 9, -10, 5), actual);
    }

}
