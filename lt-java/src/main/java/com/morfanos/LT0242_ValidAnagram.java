package com.morfanos;

class LT0242_ValidAnagram {

    static boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        // Reminder: {'a':97, 'z':122, 'A':65, 'Z': 90}
        var histogram = new int[128];
        for (var i = 0; i < s.length(); i++) {
            histogram[s.charAt(i)] += 1;
        }

        for (var i = 0; i < t.length(); i++) {
            histogram[t.charAt(i)] -= 1;
        }

        for (var i = 0; i < histogram.length; i++) {
            if (histogram[i] != 0) {
                return false;
            }
        }

        return true;
    }

}
