package com.morfanos;

class LT0383_RansomNote {

    static boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) {
            return false;
        }

        var histogram = new int[26];

        for (int i = 0; i < magazine.length(); i++) {
            histogram[magazine.charAt(i) - 'a'] += 1;
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            histogram[ransomNote.charAt(i) - 'a'] -= 1;
        }

        for (int i = 0; i < histogram.length; i++) {
            if (histogram[i] < 0) {
                return false;
            }
        }

        return true;
    }

}
