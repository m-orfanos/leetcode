package com.morfanos.solutions;

import static com.morfanos.solutions.LT0013_RomanInteger.romanToInt;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0013_RomanIntegerTest {

    @Test
    void romanToInt1() {
        var actual = romanToInt("III");
        assertEquals(3, actual);
    }

    @Test
    void romanToInt2() {
        var actual = romanToInt("MCMXCIV");
        assertEquals(1994, actual);
    }

}
