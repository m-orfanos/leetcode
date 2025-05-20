package com.morfanos.solutions;

import org.junit.jupiter.api.Test;

import static com.morfanos.shared.Helper.to1DArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0234PalindromeLinkedList.isPalindrome;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

class LT0234PalindromeLinkedListTest {

    @Test
    void isPalindrome1() {
        var a = to1DArray(1, 2, 2, 1);
        var l = toListNode(a);
        var actual = isPalindrome(l);
        assertTrue(actual);
    }

    @Test
    void isPalindrome2() {
        var a = to1DArray(1, 2);
        var l = toListNode(a);
        var actual = isPalindrome(l);
        assertFalse(actual);
    }

    @Test
    void isPalindrome3() {
        var a = to1DArray(1, 0, 1);
        var l = toListNode(a);
        var actual = isPalindrome(l);
        assertTrue(actual);
    }

}
