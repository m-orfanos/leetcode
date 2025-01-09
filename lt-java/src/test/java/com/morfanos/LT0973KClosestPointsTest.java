package com.morfanos;

import static com.morfanos.LT0973KClosestPoints.kClosest;
import static com.morfanos.shared.Helper.to2DArray;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0973KClosestPointsTest {

    @Test
    void kClosest1() {
        var points = to2DArray(1, 3, -2, 2);
        var actual = kClosest(points, 1);
        var expected = new int[][] { { -2, 2 } };
        assertArrayEquals(expected, actual);
    }

}
