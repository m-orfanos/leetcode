package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0283MoveZeroes.moveZeroes;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

class LT0283MoveZeroesTest {

    @Test
    void moveZeroes1() {
        var a = to1DArray(0, 1, 0, 3, 0, 12);
        moveZeroes(a);
        assertArrayEquals(to1DArray(1, 3, 12, 0, 0, 0), a);
    }

}
