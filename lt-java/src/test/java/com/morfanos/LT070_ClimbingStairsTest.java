package com.morfanos;

import static com.morfanos.LT070_ClimbingStairs.climbStairs1;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT070_ClimbingStairsTest {

    // Fibonacci approach
    @Test
    void climbStairs11() {
        var actual = climbStairs1(2);
        assertEquals(2, actual);
    }

    @Test
    void climbStairs12() {
        var actual = climbStairs1(8);
        assertEquals(34, actual);
    }

    @Test
    void climbStairs13() {
        var actual = climbStairs1(35);
        assertEquals(14930352, actual);
    }

    // combinatorics approach
    @Test
    void climbStairs21() {
        var s = new LT070_ClimbingStairs();
        var actual = s.climbStairs(2);
        assertEquals(2, actual);
    }

    @Test
    void climbStairs22() {
        var actual = climbStairs1(8);
        assertEquals(34, actual);
    }

    @Test
    void climbStairs23() {
        var s = new LT070_ClimbingStairs();
        var actual = s.climbStairs(35);
        assertEquals(14930352, actual);
    }

}
