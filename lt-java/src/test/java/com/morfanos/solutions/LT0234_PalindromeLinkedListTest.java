package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toArray;
import static com.morfanos.shared.Helper.toListNode;
import static com.morfanos.solutions.LT0234_PalindromeLinkedList.isPalindrome;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0234_PalindromeLinkedListTest {

    @Test
    void isPalindrome1() {
        var a = toArray(1, 2, 2, 1);
        var l = toListNode(a);
        var actual = isPalindrome(l);
        assertTrue(actual);
    }

    @Test
    void isPalindrome2() {
        var a = toArray(1, 2);
        var l = toListNode(a);
        var actual = isPalindrome(l);
        assertFalse(actual);
    }

    @Test
    void isPalindrome3() {
        var a = toArray(1, 0, 1);
        var l = toListNode(a);
        var actual = isPalindrome(l);
        assertTrue(actual);
    }

}
