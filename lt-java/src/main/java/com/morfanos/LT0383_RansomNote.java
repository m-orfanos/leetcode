package com.morfanos;

class LT0383_RansomNote {

    static boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) {
            return false;
        }

        // Reminder: {'a':97, 'z':122, 'A':65, 'Z': 90}
        var histogram = new int[128];

        for (var i = 0; i < magazine.length(); i++) {
            histogram[magazine.charAt(i)] += 1;
        }

        for (var i = 0; i < ransomNote.length(); i++) {
            histogram[ransomNote.charAt(i)] -= 1;
        }

        for (var i = 0; i < histogram.length; i++) {
            if (histogram[i] < 0) {
                return false;
            }
        }

        return true;
    }

}
