package com.morfanos;

import static com.morfanos.LT0206_ReverseLinkedList.reverseList;
import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.shared.Helper.toListNode;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0206_ReverseLinkedListTest {

    @Test
    void reverseList1() {
        var a1 = toArray(1, 2, 3, 4, 5);
        var l1 = toListNode(a1);
        var l2 = reverseList(l1);
        var a2 = toArray(l2);
        assertArrayEquals(toArray(5, 4, 3, 2, 1), a2);
    }

}
