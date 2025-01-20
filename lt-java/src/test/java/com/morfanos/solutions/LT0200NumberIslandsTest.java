package com.morfanos.solutions;

import static com.morfanos.solutions.LT0200NumberIslands.numIslands;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0200NumberIslandsTest {

    @Test
    void numIslands1() {
        var grid = new char[][] {
                { '1', '1', '1', '1', '0' },
                { '1', '1', '0', '1', '0' },
                { '1', '1', '0', '0', '0' },
                { '0', '0', '0', '0', '0' }
        };
        var actual = numIslands(grid);
        assertEquals(1, actual);
    }

}
