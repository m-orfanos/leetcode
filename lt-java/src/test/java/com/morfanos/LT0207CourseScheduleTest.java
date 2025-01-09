package com.morfanos;

import static com.morfanos.LT0207CourseSchedule.canFinish;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0207CourseScheduleTest {

    @Test
    void canFinish11() {
        var actual = canFinish(
                2,
                new int[][] { { 1, 0 } });
        assertTrue(actual);
    }

    @Test
    void canFinish12() {
        var actual = canFinish(
                2,
                new int[][] { { 1, 0 }, { 0, 1 } });
        assertFalse(actual);
    }

    @Test
    void canFinish13() {
        var actual = canFinish(
                5,
                new int[][] {
                        { 1, 4 }, { 2, 4 },
                        { 3, 1 }, { 3, 2 } });
        assertTrue(actual);
    }

    @Test
    void canFinish14() {
        var actual = canFinish(
                5,
                new int[][] { { 0, 1 }, { 0, 2 }, { 1, 2 } });
        assertTrue(actual);
    }

}
