package com.morfanos.solutions;

class LT0003LongestSubstringWithoutRepeat {

    static int lengthOfLongestSubstring1(String s) {
        var seen = new int[128];
        for (var i = 0; i < seen.length; i++) {
            seen[i] = -1;
        }

        var max = 0;

        var left = 0;
        var i = 0;
        while (i < s.length()) {
            var ch = s.charAt(i);
            if (seen[ch] != -1) {
                max = Math.max(max, i - left);
                for (var k = left; k < seen[ch]; k++) {
                    seen[s.charAt(k)] = -1;
                }
                left = seen[ch] + 1;
            }
            seen[ch] = i;
            i += 1;
        }

        return Math.max(max, i - left);
    }

    // modified approach of above
    // no need to clear the `seen` cache, can simply check if
    // the last seen is after the current left
    static int lengthOfLongestSubstring2(String s) {
        var seen = new int[128];
        for (var i = 0; i < seen.length; i++) {
            seen[i] = -1;
        }

        var max = 0;

        var left = 0;
        for (int i = 0; i < s.length(); i++) {
            var ch = s.charAt(i);
            if (seen[ch] >= left) {
                left = seen[ch] + 1;
            } else {
                max = Math.max(max, i - left + 1);
            }
            seen[ch] = i;
        }

        return max;
    }

}
