package com.morfanos;

import static com.morfanos.LT0994RottingOranges.orangesRotting;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0994RottingOrangesTest {

    @Test
    void orangesRotting1() {
        var grid = new int[][] { { 2, 1, 1 }, { 1, 1, 0 }, { 0, 1, 1 } };
        var actual = orangesRotting(grid);
        assertEquals(4, actual);
    }

}
