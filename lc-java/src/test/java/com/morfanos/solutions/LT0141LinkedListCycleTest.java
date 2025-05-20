package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0141LinkedListCycle.hasCycle;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0141LinkedListCycleTest {

    @Test
    void hasCycle1() {
        var l = toListNode(to1DArray(3, 2, 0, -4));
        var t = l.next.next.next;
        t.next = l.next;

        var actual = hasCycle(l);

        assertTrue(actual);
    }

}
