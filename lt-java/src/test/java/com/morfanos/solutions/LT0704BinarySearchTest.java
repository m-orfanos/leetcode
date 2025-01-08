package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.solutions.LT0704BinarySearch.search;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LT0704BinarySearchTest {

    @Test
    void search1() {
        var ans = search(to1DArray(-1, 0, 3, 5, 9, 12), 9);
        assertEquals(4, ans);
    }

}
