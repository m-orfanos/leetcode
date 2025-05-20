package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0383RansomNote.canConstruct;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0383RansomNoteTest {

    @Test
    void canConstruct1() {
        var actual = canConstruct("a", "b");
        assertFalse(actual);
    }

    @Test
    void canConstruct2() {
        var actual = canConstruct("aa", "ab");
        assertFalse(actual);
    }

    @Test
    void canConstruct3() {
        var actual = canConstruct("aa", "aab");
        assertTrue(actual);
    }

}
