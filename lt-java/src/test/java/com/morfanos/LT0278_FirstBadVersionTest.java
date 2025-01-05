package com.morfanos;

import static com.morfanos.LT0278_FirstBadVersion.firstBadVersion;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0278_FirstBadVersionTest {

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
