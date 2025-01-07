package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.solutions.LT0283_MoveZeroes.moveZeroes;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

class LT0283_MoveZeroesTest {

    @Test
    void moveZeroes1() {
        var a = toArray(0, 1, 0, 3, 0, 12);
        moveZeroes(a);
        assertArrayEquals(toArray(1, 3, 12, 0, 0, 0), a);
    }

}
