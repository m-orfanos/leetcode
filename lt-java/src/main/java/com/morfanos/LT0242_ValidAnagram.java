package com.morfanos;

class LT0242_ValidAnagram {

    static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        var histogram = new int[26];
        for (int i = 0; i < s.length(); i++) {
            histogram[s.charAt(i) - 'a'] += 1;
        }

        for (int i = 0; i < t.length(); i++) {
            histogram[t.charAt(i) - 'a'] -= 1;
        }

        for (int i = 0; i < histogram.length; i++) {
            if (histogram[i] != 0) {
                return false;
            }
        }

        return true;
    }

}
