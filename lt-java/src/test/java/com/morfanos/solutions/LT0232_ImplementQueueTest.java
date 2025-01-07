package com.morfanos.solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

import org.junit.jupiter.api.Test;

class LT0232_ImplementQueueTest {

    @Test
    void test1() {
        var q = new LT0232_ImplementQueue.MyQueue();
        q.push(1);
        q.push(2);

        assertEquals(1, q.peek());
        assertEquals(1, q.pop());
        assertFalse(q.empty());
    }

}
