package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0070ClimbingStairs.climbStairs;
import static com.morfanos.solutions.LT0070ClimbingStairs.climbStairs1;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0070ClimbingStairsTest {

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
        var actual = climbStairs(2);
        assertEquals(2, actual);
    }

    @Test
    void climbStairs22() {
        var actual = climbStairs1(8);
        assertEquals(34, actual);
    }

    @Test
    void climbStairs23() {
        var actual = climbStairs(35);
        assertEquals(14930352, actual);
    }

}
