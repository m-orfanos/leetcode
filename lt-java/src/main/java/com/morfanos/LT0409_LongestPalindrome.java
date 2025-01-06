package com.morfanos;

class LT0409_LongestPalindrome {

    static int longestPalindrome(String s) {
        // Reminder: {'a':97, 'z':122, 'A':65, 'Z': 90}
        var histogram = new int[128];
        for (int i = 0; i < s.length(); i++) {
            histogram[s.charAt(i)] += 1;
        }

        var len = 0;
        for (int i = 0; i < histogram.length; i++) {
            len += histogram[i] / 2;
        }

        len *= 2;

        if (len < s.length()) {
            // if the string has only even-numbered characters
            // then `len` will always equals the string's length
            len += 1;
        }

        return len;
    }

}
