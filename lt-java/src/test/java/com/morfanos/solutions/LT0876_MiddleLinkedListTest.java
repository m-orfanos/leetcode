package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0876_MiddleLinkedList.middleNode;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0876_MiddleLinkedListTest {

    @Test
    void middleNode1() {
        var l = toListNode(toArray(1, 2, 3, 4, 5));
        var actual = middleNode(l);
        assertEquals(3, actual.val);
    }

    @Test
    void middleNode2() {
        var l = toListNode(toArray(1, 2, 3, 4, 5, 6));
        var actual = middleNode(l);
        assertEquals(4, actual.val);
    }

}
