package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0013RomanInteger.romanToInt;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0013RomanIntegerTest {

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
