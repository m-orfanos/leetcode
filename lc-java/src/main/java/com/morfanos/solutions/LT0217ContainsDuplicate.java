package com.morfanos.solutions;

import java.util.Arrays;

class LT0217ContainsDuplicate {

    static boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (var i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }

        }
        return false;
    }

}
