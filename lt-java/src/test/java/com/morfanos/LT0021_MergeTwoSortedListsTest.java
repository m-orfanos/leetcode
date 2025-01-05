package com.morfanos;

import static com.morfanos.LT0021_MergeTwoSortedLists.mergeTwoLists;
import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.shared.Helper.toListNode;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0021_MergeTwoSortedListsTest {

    @Test
    void mergeTwoLists1() {
        var l1 = toListNode(toArray(1, 2, 4));
        var l2 = toListNode(toArray(1, 3, 4));
        var l3 = mergeTwoLists(l1, l2);
        var ans = toArray(l3);
        assertArrayEquals(toArray(1, 1, 2, 3, 4, 4), ans);
    }

    @Test
    void mergeTwoLists2() {
        var l1 = toListNode(toArray(-9, 3));
        var l2 = toListNode(toArray(5, 7));
        var l3 = mergeTwoLists(l1, l2);
        var ans = toArray(l3);
        assertArrayEquals(toArray(-9, 3, 5, 7), ans);
    }

}
