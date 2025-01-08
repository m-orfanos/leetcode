package com.morfanos;

import static com.morfanos.LT0057_InsertInterval.insert;
import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.shared.Helper.to2DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0057_InsertIntervalTest {

    @Test
    void insert1() {
        var intervals = to2DArray(1, 3, 6, 9);
        var newInterval = toArray(2, 5);
        var actual = insert(intervals, newInterval);
        var expected = to2DArray(1, 5, 6, 9);
        assertArrayEquals(expected, actual);
    }

}
