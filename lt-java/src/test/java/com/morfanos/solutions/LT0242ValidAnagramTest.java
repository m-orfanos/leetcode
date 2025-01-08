package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.solutions.LT0242ValidAnagram.isAnagram;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0242ValidAnagramTest {

    @Test
    void isAnagram1() {
        var ans = isAnagram("anagram", "nagaram");
        assertTrue(ans);
    }

}
