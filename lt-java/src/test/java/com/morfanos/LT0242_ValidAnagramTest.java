package com.morfanos;

import static com.morfanos.LT0242_ValidAnagram.isAnagram;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0242_ValidAnagramTest {

    @Test
    void isAnagram1() {
        var ans = isAnagram("anagram", "nagaram");
        assertTrue(ans);
    }

}
