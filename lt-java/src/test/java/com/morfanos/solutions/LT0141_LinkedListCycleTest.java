package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0141_LinkedListCycle.hasCycle;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0141_LinkedListCycleTest {

    @Test
    void hasCycle1() {
        var l = toListNode(toArray(3, 2, 0, -4));
        var t = l.next.next.next;
        t.next = l.next;

        var actual = hasCycle(l);

        assertTrue(actual);
    }

}
