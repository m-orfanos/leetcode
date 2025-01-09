package com.morfanos.solutions;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0015ThreeSum.threeSum1;
import static com.morfanos.solutions.LT0015ThreeSum.threeSum2;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Comparator;
import java.util.List;

import org.junit.jupiter.api.Test;

class LT0015ThreeSumTest {

    @Test
    void threeSum11() {
        var actual = threeSum1(to1DArray(-1, 0, 1, 2, -1, -4));
        var expected = List.of(
                List.of(-1, 0, 1),
                List.of(-1, -1, 2));
        assertEquals(expected, actual);
    }

    @Test
    void threeSum12() {
        var actual = threeSum1(to1DArray(0, 1, 1));
        var expected = List.of();
        assertEquals(expected, actual);
    }

    @Test
    void threeSum13() {
        var actual = threeSum1(to1DArray(0, 0, 0));
        var expected = List.of(List.of(0, 0, 0));
        assertEquals(expected, actual);
    }

    private Comparator<? super List<Integer>> asc() {
        return (a, b) -> {
            if (a.get(0) == b.get(0)) {
                return a.get(1) - b.get(1);
            } else {
                return a.get(0) - b.get(0);
            }
        };
    }

    @Test
    void threeSum14() {
        var actual = threeSum1(to1DArray(-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4));
        actual.sort(asc());

        var expected = List.of(
                List.of(-4, 0, 4),
                List.of(-4, 1, 3),
                List.of(-3, -1, 4),
                List.of(-3, 0, 3),
                List.of(-3, 1, 2),
                List.of(-2, -1, 3),
                List.of(-2, 0, 2),
                List.of(-1, -1, 2),
                List.of(-1, 0, 1));

        assertEquals(expected, actual);
    }

    @Test
    void threeSum24() {
        var actual = threeSum2(to1DArray(-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4));
        var expected = List.of(
                List.of(-4, 0, 4),
                List.of(-4, 1, 3),
                List.of(-3, -1, 4),
                List.of(-3, 0, 3),
                List.of(-3, 1, 2),
                List.of(-2, -1, 3),
                List.of(-2, 0, 2),
                List.of(-1, -1, 2),
                List.of(-1, 0, 1));
        assertEquals(expected, actual);
    }

}
