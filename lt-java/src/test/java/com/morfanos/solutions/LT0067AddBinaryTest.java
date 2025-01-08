package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0067AddBinary.addBinary;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0067AddBinaryTest {

    @Test
    void addBinary1() {
        var actual = addBinary("11", "1");
        assertEquals("100", actual);
    }

    @Test
    void addBinary2() {
        var actual = addBinary("1010", "1011");
        assertEquals("10101", actual);
    }

    @Test
    void addBinary3() {
        var actual = addBinary(
                "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
                "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011");
        assertEquals(
                "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000",
                actual);
    }

}
