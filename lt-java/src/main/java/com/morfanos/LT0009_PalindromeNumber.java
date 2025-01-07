package com.morfanos;

class LT0009_PalindromeNumber {

    static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        var cpy = x;
        var rev = 0;
        while (cpy > 0) {
            rev = 10 * rev + cpy % 10;
            cpy /= 10;
        }
        return rev == x;
    }

}
