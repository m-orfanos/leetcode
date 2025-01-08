package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0206ReverseLinkedList.reverseList;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0206ReverseLinkedListTest {

    @Test
    void reverseList1() {
        var a1 = to1DArray(1, 2, 3, 4, 5);
        var l1 = toListNode(a1);
        var l2 = reverseList(l1);
        var a2 = to1DArray(l2);
        assertArrayEquals(to1DArray(5, 4, 3, 2, 1), a2);
    }

}
