package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0876MiddleLinkedList.middleNode;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0876MiddleLinkedListTest {

    @Test
    void middleNode1() {
        var l = toListNode(to1DArray(1, 2, 3, 4, 5));
        var actual = middleNode(l);
        assertEquals(3, actual.val);
    }

    @Test
    void middleNode2() {
        var l = toListNode(to1DArray(1, 2, 3, 4, 5, 6));
        var actual = middleNode(l);
        assertEquals(4, actual.val);
    }

}
