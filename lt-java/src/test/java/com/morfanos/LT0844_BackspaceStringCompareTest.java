package com.morfanos;

import static com.morfanos.LT0844_BackspaceStringCompare.backspaceCompare;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0844_BackspaceStringCompareTest {

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
