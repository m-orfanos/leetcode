package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0844BackspaceStringCompare.backspaceCompare;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0844BackspaceStringCompareTest {

    @Test
    void backspaceCompare1() {
        var actual = backspaceCompare("ab#c", "ad#c");
        assertTrue(actual);
    }

    @Test
    void backspaceCompare2() {
        var actual = backspaceCompare("ab##", "c#d#");
        assertTrue(actual);
    }

    @Test
    void backspaceCompare3() {
        var actual = backspaceCompare("a#c", "b");
        assertFalse(actual);
    }

}
