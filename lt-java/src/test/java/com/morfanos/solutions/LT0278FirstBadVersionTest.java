package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0278FirstBadVersion.firstBadVersion;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0278FirstBadVersionTest {

    @Test
    void firstBadVersion1() {
        var actual = firstBadVersion(5, (n) -> n == 4);
        assertEquals(4, actual);
    }

    @Test
    void firstBadVersion2() {
        var actual = firstBadVersion(1, (n) -> n == 1);
        assertEquals(1, actual);
    }

}
