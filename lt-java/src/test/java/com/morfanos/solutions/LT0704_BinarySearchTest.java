package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.solutions.LT0704_BinarySearch.search;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class LT0704_BinarySearchTest {

    @Test
    void search1() {
        var ans = search(toArray(-1, 0, 3, 5, 9, 12), 9);
        assertEquals(4, ans);
    }

}
