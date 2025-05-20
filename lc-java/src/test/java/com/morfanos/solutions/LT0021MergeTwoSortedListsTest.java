package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0021MergeTwoSortedLists.mergeTwoLists;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0021MergeTwoSortedListsTest {

    @Test
    void mergeTwoLists1() {
        var l1 = toListNode(to1DArray(1, 2, 4));
        var l2 = toListNode(to1DArray(1, 3, 4));
        var l3 = mergeTwoLists(l1, l2);
        var ans = to1DArray(l3);
        assertArrayEquals(to1DArray(1, 1, 2, 3, 4, 4), ans);
    }

    @Test
    void mergeTwoLists2() {
        var l1 = toListNode(to1DArray(-9, 3));
        var l2 = toListNode(to1DArray(5, 7));
        var l3 = mergeTwoLists(l1, l2);
        var ans = to1DArray(l3);
        assertArrayEquals(to1DArray(-9, 3, 5, 7), ans);
    }

}
