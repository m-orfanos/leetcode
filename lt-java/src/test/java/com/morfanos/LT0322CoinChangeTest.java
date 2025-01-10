package com.morfanos;

import static com.morfanos.LT0322CoinChange.coinChange;
import static com.morfanos.shared.Helper.to1DArray;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0322CoinChangeTest {

    @Test
    void coinChange1() {
        var actual = coinChange(to1DArray(1, 2, 5), 11);
        assertEquals(3, actual);
    }

    @Test
    void coinChange2() {
        var actual = coinChange(to1DArray(186, 419, 83, 408), 6249);
        assertEquals(20, actual);
    }

    @Test
    void coinChange3() {
        var actual = coinChange(to1DArray(411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422), 9864);
        assertEquals(24, actual);
    }

}
