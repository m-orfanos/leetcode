package com.morfanos.solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0155MinStackTest {

    @Test
    void minStackTest1() {
        var s = new LT0155MinStack.MinStack();

        s.push(-2);
        s.push(0);
        s.push(-3);

        assertEquals(-3, s.getMin());

        s.pop();

        assertEquals(0, s.top());
        assertEquals(-2, s.getMin());
    }

    @Test
    void minStackTest2() {
        var s = new LT0155MinStack.MinStack();

        s.push(-2);
        s.push(0);
        s.push(-1);

        assertEquals(-2, s.getMin());
        assertEquals(-1, s.top());

        s.pop();

        assertEquals(-2, s.getMin());
    }

    @Test
    void minStackTest3() {
        var s = new LT0155MinStack.MinStack();

        s.push(2);
        s.push(0);
        s.push(3);
        s.push(0);

        assertEquals(0, s.getMin());
        s.pop();

        assertEquals(0, s.getMin());
        s.pop();

        assertEquals(0, s.getMin());
        s.pop();

        assertEquals(2, s.getMin());
    }

}
