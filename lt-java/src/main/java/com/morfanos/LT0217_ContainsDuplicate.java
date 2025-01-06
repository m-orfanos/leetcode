package com.morfanos;

import java.util.Arrays;

class LT0217_ContainsDuplicate {

    static boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }

        }
        return false;
    }

}
