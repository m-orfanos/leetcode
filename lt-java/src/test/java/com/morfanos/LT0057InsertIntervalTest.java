package com.morfanos;

import org.junit.jupiter.api.Test;

import static com.morfanos.LT0057InsertInterval.insert;
import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.shared.Helper.to2DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0057InsertIntervalTest {

    @Test
    void insert1() {
        var intervals = to2DArray(1, 3, 6, 9);
        var newInterval = to1DArray(2, 5);
        var actual = insert(intervals, newInterval);
        var expected = to2DArray(1, 5, 6, 9);
        assertArrayEquals(expected, actual);
    }

}
