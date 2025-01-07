package com.morfanos.solutions;

import static com.morfanos.solutions.LT0383_RansomNote.canConstruct;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0383_RansomNoteTest {

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
